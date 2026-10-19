# ACDRL-CORE-001 — Core Architecture Research and Validation Protocol

**Version:** 0.1 | **Status:** Design protocol, not executed.

## Central question
Can a modular, safety-constrained cyber-defense core process common observation contracts and produce reproducible, auditable, non-disruptive decisions in two heterogeneous simulated domains while preserving each domain's operational constraints?

## Immediate engineering question
Can an advisory-only MVP process deterministic synthetic event fixtures end to end without leaking domain-specific logic into the common core?

## Hypotheses
- **H1 — Contract conformance:** valid spacecraft and financial fixtures are processed through the same core interfaces; invalid fixtures fail safely and are auditable.
- **H2 — Safety:** unknown or disruptive proposed actions never pass the MVP safety gate; no real actuation occurs.
- **H3 — Reproducibility:** identical code, configuration and fixtures produce identical canonical outputs and decision traces.
- **H4 — Adaptability (later):** integration of a second domain is possible through adapter/policy changes without changing core decision-pipeline interfaces. This is a hypothesis to test, not an assumed result.

## Study design
### Stage A — Contract and policy review
Specify JSON schemas, versioning, identity/provenance boundaries, failure semantics, safety gate and permitted advisory actions. Establish literature matrix on modular security architecture, safe decisions, cyber-physical resilience and transfer.

### Stage B — Deterministic MVP
Implement observation ingestion → context → rule detection → transparent risk priority → candidate advisory → independent safety veto → audit. Use fixture-driven unit and integration tests.

### Stage C — Domain adapter validation
Create a spacecraft fixture adapter and a financial payment-event fixture adapter. Run the same core without domain-specific conditional branches in core modules. Record any necessary contract changes.

### Stage D — Empirical evaluation
When real simulators are implemented, evaluate within-domain baselines, false alarms, missed events, safety violations, runtime and reproducibility. Use held-out scenario families and multiple seeds before discussing generalization.

## Minimal test fixtures
1. Valid normal observation → NO_ACTION.
2. Repeated rejected-command observations → advisory or human review according to declared rule.
3. Malformed or unknown-schema observation → rejected and logged.
4. Proposed disruptive action → safety veto, no execution.
5. Missing policy or unavailable adapter → fail closed, audit record.
6. Equivalent financial-domain fixture → same contract path with domain-specific mapping.
7. Repeat identical run → matching canonical hashes.

## Baselines
- Schema-only validation (no detection).
- Deterministic rule detection and simple priority mapping.
- NO_ACTION-only policy for measuring unnecessary alerts and risk tradeoffs.
Advanced ML or RL is deferred until baseline behavior is established.

## Evaluation metrics
Contract acceptance/rejection correctness; unit/integration test pass rate; safety veto correctness; unauthorized execution count (target zero); decision-trace completeness; deterministic hash equality; processing latency; number and nature of domain-specific core changes; later precision/recall and false-alarm rates against independent ground truth.

## Data separation
Synthetic scenario labels and injection metadata remain in evaluator-only records. The online core receives only observations and declared context available at decision time. Do not treat arbitrary synthetic scores as calibrated probabilities.

## Reproducibility evidence
Record protocol version, source commit SHA, environment/dependencies, fixture hashes, configuration/policy versions, test results, canonical output hashes, failures and limitations. Index executed results in EXPERIMENT_REGISTRY.md and EVIDENCE_REGISTER.md.

## Acceptance gate
Core modules and contracts reviewed; both fixture types accepted; fail-closed tests passed; safety policy independent of decision model; deterministic outputs confirmed; no live integrations. These criteria cannot be marked complete before implementation and testing.

## Limits and claims
A working common API demonstrates modular engineering, not cross-domain detection effectiveness or scientific novelty. Generalization and operational safety require separate experiments and independent validation.

## Next milestone
Implement `src/acdrl_core/` and `tests/` after owner approval, beginning with the advisory-only deterministic MVP. Keep the existing spacecraft mathematical and simulation documents as the first domain testbed specifications.

**Related:** [Core architecture](../core/CORE_ARCHITECTURE.md) · [Interface contracts](../core/INTERFACE_CONTRACTS.md).
