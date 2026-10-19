# ACDRL-CORE-001 — Domain-Independent Interface Contracts

**Version:** 0.1 | **Status:** Draft schema design; examples are illustrative, not generated output.

## 1. Shared conventions
- JSON-compatible records with explicit `schema_version`, `domain_id`, `run_id`, `event_id`, `step`, and `source`.
- Event time is an integer simulation step for deterministic fixtures; wall-clock capture time, if used, is separate.
- All IDs are strings, steps nonnegative integers, numeric scores finite.
- A domain adapter may add namespaced `attributes`, but the core must not depend on undocumented domain-specific keys.
- Reject malformed records and log rejection reasons; never silently coerce security-critical fields.
- A field named `actor_id` is not proof of identity or authentication.

## 2. Observation
```json
{
  "schema_version": "0.1",
  "domain_id": "spacecraft",
  "run_id": "fixture-001",
  "event_id": "evt-001",
  "step": 10,
  "source": "sim-ground-station",
  "event_type": "command_validation",
  "asset_id": "SIM-SC-001",
  "attributes": {"authorization_result": "denied"},
  "quality": {"synthetic": true, "missing_fields": false}
}
```
The `attributes` dictionary is adapter-owned. The core must use declared feature extraction or policy mappings rather than hard-coded spacecraft field names.

## 3. ContextState
```json
{
  "schema_version": "0.1",
  "domain_id": "spacecraft",
  "run_id": "fixture-001",
  "step": 10,
  "asset_id": "SIM-SC-001",
  "feature_values": {"rejected_command_count_window": 3},
  "feature_quality": {"rejected_command_count_window": "observed"},
  "policy_context_id": "sc-policy-v0"
}
```
Context includes only information available at or before the decision step. Missing values and stale data must be explicit.

## 4. Finding and RiskAssessment
```json
{
  "schema_version": "0.1",
  "finding_id": "finding-001",
  "observation_refs": ["evt-001"],
  "detector_id": "rule-denied-commands-v0",
  "detector_version": "0.1",
  "signal": "repeated_denied_commands",
  "score": 0.7,
  "score_semantics": "uncalibrated_priority",
  "uncertainty": "not_estimated"
}
```
A risk assessment adds declared asset impact, rationale, assumptions, priority band and uncertainty. A numeric score is **not** a probability unless separately calibrated and validated.

## 5. CandidateDecision and SafetyVerdict
```json
{
  "schema_version": "0.1",
  "decision_id": "decision-001",
  "finding_refs": ["finding-001"],
  "proposed_action": "ALERT_OPERATOR",
  "policy_version": "core-policy-v0",
  "rationale": "Repeated rejected commands in the configured observation window"
}
```
```json
{
  "schema_version": "0.1",
  "decision_id": "decision-001",
  "verdict": "ADVISORY_ALLOWED",
  "requires_human_approval": false,
  "executed": false,
  "safety_policy_version": "safety-v0",
  "reason_code": "NON_DISRUPTIVE_ADVISORY"
}
```
Initial allowed decisions: `NO_ACTION`, `ALERT_OPERATOR`, `REQUEST_HUMAN_REVIEW`. Any other action must be vetoed by the MVP safety gate. No physical or payment-system action is performed.

## 6. ActionOutcome and EvidenceRecord
`ActionOutcome` records whether an approved action was attempted, its authorization source, result, and reason; advisory output must record `executed=false` for operational actuation. `EvidenceRecord` links observation, finding, risk, decision, verdict, code commit, configuration hash, run seed, and test result. Never embed secrets in logs.

## 7. Failure semantics
| Condition | Mandatory behavior |
| --- | --- |
| Unknown schema version | Reject with audit event |
| Missing or nonfinite security-critical field | Reject or mark unavailable; do not assume safe |
| Duplicate event ID | Idempotent handling or explicit rejection |
| Out-of-order event | Apply documented ordering policy; do not use future observations |
| Missing safety policy | No execution; emit error and request review |
| Unknown proposed action | Veto; no execution |
| Adapter unavailable | No execution; preserve audit trail |
| Ground-truth label exposed to core | Fail experiment validation |

## 8. Adapter conformance tests
Both domains must produce valid observations, map local constraints into declared policy context, reject malformed events, and support deterministic fixtures. Domain-specific telemetry and transaction schemas remain separate from this common contract.

## 9. Versioning
Breaking field or semantic changes require a new schema version, migration notes, and tests. A model version and a policy version must be recorded independently.

**Related:** [Core architecture](CORE_ARCHITECTURE.md) · [Research protocol](../protocols/ACDRL-CORE-001.md).
