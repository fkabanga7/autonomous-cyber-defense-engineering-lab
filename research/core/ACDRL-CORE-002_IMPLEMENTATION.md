# ACDRL-CORE-002 — Implementation Record

**Status:** Implemented; preliminary unit verification completed  
**Baseline revision:** `8c12e886b802cc046e8eb1aaaafa8726c594ac89`  
**Date of documentation:** 2026-10-22  
**Scope:** Deterministic, advisory-only Python minimum viable prototype (MVP)

## 1. Purpose and boundary

CORE-002 implements a small, inspectable processing core following the CORE-001 architectural separation of ingestion, detection, prioritization, decision, independent safety checking, and audit serialization. It does not implement live actuation, machine learning, temporal correlation, probabilistic uncertainty, spacecraft-specific telemetry adapters, or financial-system integrations.

## 2. Source inventory

| Module | Function | Observed behavior |
|---|---|---|
| `src/acdrl_core/models.py` | Data contracts | Frozen dataclasses `Observation`, `Finding`, `RiskAssessment`, `CandidateDecision`, `SafetyVerdict`; action allowlist |
| `src/acdrl_core/ingestion.py` | `ingest` | Validates mapping, required nonblank strings, schema `0.1`, exact nonnegative `int` step, dictionary attributes; copies top-level attributes dictionary |
| `src/acdrl_core/detection.py` | `detect` | Emits a finding for `event_type == "authorization_denied"`, with fixed score `0.7`; otherwise `None` |
| `src/acdrl_core/risk.py` | `assess` | `HIGH` when finding score `>= 0.8`, otherwise `MEDIUM`; no finding returns `None` |
| `src/acdrl_core/decision.py` | `decide` | No risk → `NO_ACTION`; `HIGH` → `REQUEST_HUMAN_REVIEW`; all other non-null risk priorities → `ALERT_OPERATOR` |
| `src/acdrl_core/safety.py` | `check` | Missing policy → `MISSING_POLICY`; action outside allowlist → `ACTION_NOT_PERMITTED`; permitted advisory → `ADVISORY_ONLY`; always `executed=False` |
| `src/acdrl_core/audit.py` | `audit_record` | JSON with sorted keys, compact separators, `allow_nan=False` |
| `src/acdrl_core/pipeline.py` | `process` | Sequential orchestration; returns serialized audit string |

## 3. Processing sequence

```text
Untrusted mapping
  → ingest(record)
  → detect(observation)
  → assess(finding)
  → decide(risk)
  → check(candidate, policy_available=...)
  → audit_record(...)
  → JSON string
```

The observation fields are `schema_version`, `domain_id`, `run_id`, `event_id`, `step`, `source`, `event_type`, `asset_id`, and optional `attributes` (default `{}`). The seven string fields must be nonblank; `step` must be an integer `>= 0` and must not be a boolean. The current schema version is exactly `0.1`. The `source` field is untrusted metadata, not source authentication.

The `Finding.score` value of `0.7` is **an uncalibrated priority**, not a probability of attack. For the only currently detected signal, `0.7 < 0.8`, so the ordinary resulting candidate is `ALERT_OPERATOR`. The `HIGH` path exists in the risk/decision code but is not produced by this fixed detector.

## 4. Safety and trust boundaries

The allowlist is `NO_ACTION`, `ALERT_OPERATOR`, and `REQUEST_HUMAN_REVIEW`. `check` is a separate function from `decide`, and it vetoes candidates when policy is unavailable or an action is not allowed. All safety verdicts set `executed=False`; there is no operational action execution path. This is a software-level boundary, **not** a demonstration of deployment safety.

Frozen dataclasses prevent ordinary field reassignment but do not guarantee deep immutability of nested dictionaries. Input validation does not authenticate producers or semantically validate arbitrary domain-specific attributes.

## 5. Audit contract

The JSON output contains `schema_version`, `run_id`, `event_id`, `domain_id`, `finding`, `risk`, `decision`, and `safety`. Repeated identical inputs are expected to produce identical JSON under this deterministic baseline. The module does not provide durable storage, tamper resistance, signing, or complete runtime provenance.

## 6. Test inventory

- `tests/test_ingestion.py`: four tests covering valid input, unsupported schema, boolean step rejection, and missing required field.
- `tests/test_detection.py`: four pipeline tests covering no-action heartbeat, denial alert, two synthetic domain labels, and repeatability.
- `tests/test_safety.py`: three tests covering allowed advisory nonexecution, veto of `BLOCK_TRANSACTION`, and missing-policy fail-closed behavior.

The eleven tests are necessary preliminary checks, not a complete specification or security assurance case.

## 7. Explicit exclusions and next stage

Not implemented: temporal context, duplicate handling across event histories, multi-event detection, configurable rule evaluation, calibrated uncertainty, safety-constrained optimization, real domain adapters, action execution, adversarial evaluation, performance benchmarks, or independent replication.

**Next milestone:** CORE-003 temporal context and configurable detection, while preserving CORE-002 behavior as a regression baseline.

## 8. Repository evidence

Source repository: `https://github.com/fkabanga7/autonomous-cyber-defense-engineering-lab`  
Baseline commit: `8c12e886b802cc046e8eb1aaaafa8726c594ac89`  
Related architecture: `research/core/CORE_ARCHITECTURE.md`, `research/core/INTERFACE_CONTRACTS.md`, `research/protocols/ACDRL-CORE-001.md`.
