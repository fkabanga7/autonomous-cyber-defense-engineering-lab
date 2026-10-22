# ACDRL-CORE-003 — Temporal Context and Configurable Detection

**Version:** 0.1 | **Status:** Engineering design awaiting implementation and tests.

## Objective
Extend CORE-002 from per-event, stateless detection to bounded temporal context with configurable rules and explicit observation quality. Keep the reusable core domain-independent and advisory-only.

## Components
1. **Event identity and ordering:** deduplicate by (domain_id, run_id, event_id); define event-time step ordering, bounded lateness and rejected-event audit. Distinguish duplicates from repeated legitimate activity.
2. **Context engine:** retain a bounded window per (domain_id, run_id, asset_id), plus optional explicitly declared cross-asset correlation keys. No implicit data sharing between domains or runs.
3. **Feature extraction:** compute counts, rates, gaps, distinct assets, sequence patterns and missing-observation indicators from prior/current observations only. Adapter maps native fields into versioned common features.
4. **Configurable rule engine:** load versioned, schema-validated policy configuration; deterministic thresholds/window sizes; default reject on invalid rules.
5. **Uncertainty and provenance:** represent missingness, source trust status and coverage explicitly. No fabricated posterior probabilities or calibration claims.
6. **Safety and audit:** preserve independent safety gate; record contributing event IDs, rule version, context horizon, policy decision and failure reason.

## Proposed interface additions
- `ContextState`: schema_version, domain_id, run_id, asset_id, step, window_start, feature_values, feature_quality, contributing_event_ids, context_version.
- `DetectionRule`: rule_id, rule_version, feature_name, operator, threshold, window_steps, priority_mapping.
- `Finding` additions: rule_id, contributing_event_ids, score_semantics, uncertainty_status.
- `AuditRecord` additions: rule_version, policy_version, context_hash, decision_reason.

Contract updates must be versioned and backward compatibility tested.

## Failure semantics
Duplicate event: no double counting, audit outcome. Out-of-order beyond tolerance: reject or quarantine according to documented policy. Missing context/policy: no disruptive action and explicit review signal. No ground-truth labels accessible to the online core. Context memory bounded to avoid resource exhaustion.

## Unit and integration tests
- Normal event sequence: no finding.
- Distributed low-frequency synthetic sequence: contextual rule triggers at declared threshold; stateless baseline does not.
- Benign maintenance sequence: expected control outcome.
- Duplicate ID: idempotent handling.
- Out-of-order steps: deterministic documented handling.
- Missing/corrupted input: reject or mark unknown, no implicit safe assumption.
- Spacecraft and financial adapters: same core contracts, different declared mappings.
- Replay same sequence/config: identical canonical audit output.
- Unknown proposed action or missing safety policy: veto/no execution.
- Evaluator-only ground truth: never exposed to detection.

## Exit gate
Documented schema and policies; passing deterministic tests; bounded-memory behavior; comparison against CORE-002 baseline; traceable results with exact commit and fixture hashes. No claims of real-world stealth-detection accuracy or autonomous operational defense.

## Next
After CORE-003: uncertainty calibration and abstention (CORE-004); safety-constrained decision optimization (CORE-005); Monte Carlo and transfer evaluation (CORE-006 and domain testbeds).

**Research protocol:** [ACDRL-STEALTH-001](../protocols/ACDRL-STEALTH-001.md).
