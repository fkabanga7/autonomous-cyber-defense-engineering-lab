# ACDRL-CORE-001 — Reusable Cyber-Defense Core Architecture

**Version:** 0.1 | **Status:** Proposed engineering specification; not implemented or validated.

## 1. Purpose
Define a domain-independent, safety-aware defense framework that can process observations, estimate risk, recommend actions, and record decisions without embedding spacecraft-specific or payment-system-specific assumptions in core logic. Domain adapters translate native events and enforce operational policies.

## 2. Design invariants
- **Default deny for execution:** all outputs are advisory unless a domain adapter explicitly exposes an approved, authorized action capability.
- **Safety before execution:** an independent safety gate may veto or require human approval regardless of decision-model confidence.
- **No hidden domain coupling:** the core consumes versioned common contracts; domain-specific constraints are passed explicitly.
- **Auditability:** each alert, decision, veto and outcome references the observation(s), policy version, configuration and code revision.
- **Graceful degradation:** invalid data, unknown action, missing policy or unavailable adapter means no disruptive action.
- **Reproducibility:** deterministic reference fixtures precede stochastic/learning approaches.

## 3. Core processing pipeline
```text
DOMAIN A (spacecraft)          DOMAIN B (financial payments)
         |                                  |
    adapter A                            adapter B
         +---------------+------------------+
                         |
                Observation ingestion
                         |
              Schema and provenance checks
                         |
             Context/state representation
                         |
          Detection + uncertainty estimate
                         |
               Risk/context assessment
                         |
           Candidate action / no-action
                         |
          INDEPENDENT SAFETY POLICY GATE
                         |
         advisory / deny / request approval
                         |
              Authorized response adapter
                         |
          Outcome, audit and evaluation log
```
The response adapter is **not enabled** for real-world actuation in the initial milestone.

## 4. Modules and responsibilities
| Module | Input | Output | Responsibility |
| --- | --- | --- | --- |
| Ingestion | Raw adapter event | Observation | Validate, normalize, preserve provenance |
| Context | Observations and declared domain metadata | ContextState | Maintain bounded, timestamped state |
| Detection | ContextState, rules/models | Finding | Signal anomaly and uncertainty; do not infer attacker intent without evidence |
| Risk | Findings, asset criticality, domain impact | RiskAssessment | Explain consequence and uncertainty |
| Decision | RiskAssessment, allowed action catalog | CandidateDecision | Rank no-action, advisory or mitigation candidates |
| Safety gate | CandidateDecision, policy, constraints | SafetyVerdict | Allow advisory, veto, or require human approval |
| Response | Approved verdict, adapter capability | ActionOutcome | Enforce authorization; initially advisory-only |
| Audit/evaluation | All stage outputs | EvidenceRecord | Trace decisions, calculate metrics and preserve failures |

## 5. Trust boundaries
1. Untrusted domain events to ingestion: schema validation and provenance; never assume source claims are authenticated.
2. Ingestion to context: event time and ordering, replay and duplication handling.
3. Detection to decision: uncalibrated scores are not probabilities; uncertainty must be represented explicitly.
4. Decision to safety gate: model proposals are untrusted recommendations, not permissions.
5. Safety gate to adapter: adapter must independently enforce action authorization and local invariants.
6. Experiment labels to evaluation: ground-truth scenario metadata is inaccessible to online detection and decision modules.

## 6. Minimal viable core (MVP)
- Versioned observation and context structures.
- Deterministic rule-based detector for synthetic fixture events.
- Transparent, configurable risk scoring with no claim of calibration.
- Decision choices: NO_ACTION, ALERT_OPERATOR, REQUEST_HUMAN_REVIEW.
- Independent safety gate rejecting all unrecognized/disruptive actions.
- Append-only audit records and deterministic test harness.
- No ML, RL, autonomous blocking or operational integrations in the MVP.

## 7. Domain adapters
**Spacecraft adapter:** maps telemetry, commands, communication state and safety constraints from the provisional spacecraft simulator. Example safe action: raise advisory; no live spacecraft command capability.

**Financial adapter:** maps synthetic payment events, authorization outcomes, queue/settlement indicators and continuity constraints. Example safe action: raise advisory; no live transaction blocking capability.

Both adapters must pass the same interface conformance tests, while retaining separate scenario and safety evaluations.

## 8. Evaluation design
Compare core components against simple baselines within each domain; measure schema errors, detection false alarms/misses, decision consistency, veto correctness, runtime and domain adaptation effort. Evaluate transfer with explicit held-out domain scenarios and report failure cases. Claims of transferability require evidence beyond passing identical toy fixtures.

## 9. Open questions and literature review
Investigate related architectures (e.g., security orchestration, policy engines, assurance cases, constrained decision-making, safe RL and cross-domain transfer) before claiming novelty. Decide whether common risk scales can be meaningfully compared across domains and how uncertainty is calibrated.

## 10. Milestone gate
Review [interface contracts](INTERFACE_CONTRACTS.md) and [protocol](../protocols/ACDRL-CORE-001.md); approve fixtures, safety policy and schema before implementing the first Python core.
