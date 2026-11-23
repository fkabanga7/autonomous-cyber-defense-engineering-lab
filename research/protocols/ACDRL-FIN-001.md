# ACDRL-FIN-001 — Financial Payment-System Boundary, Scenarios and Constraints

**Version:** 0.1 | **Status:** Draft for review; not executed, not approved.  
**Domain:** Critical financial payment infrastructure (isolated software simulation with synthetic events).  
**Parent documents:** `PROJECT_CHARTER.md`, `research/core/CORE_ARCHITECTURE.md`, `research/protocols/ACDRL-STEALTH-001.md`.

## 1. Purpose
Define the system boundary, assumptions, threat scenarios, observations, defensive actions and hard constraints of the first validation testbed, so that the CORE-003 comparison (hypothesis H1) and later experiments are specified before any data are generated.

This is a **specification** milestone. It does not claim realism, detection performance or operational safety.

## 2. Research question
Can a simplified, synthetic payment-system model support reproducible differentiation between normal operation, benign disturbances and security-relevant event sequences, while representing the operational constraints that limit defensive actions?

## 3. Reference system (abstract)
A deliberately generic model, not a replica of any real institution or product:

| Component | Role in the model |
| --- | --- |
| Client channel / API gateway | Entry point for authentication and payment requests |
| Authentication service | Credential verification and step-up verification |
| Transaction-processing engine | Authorization and execution of payment requests |
| Payment switch / interbank interface | Message exchange with external counterparties |
| Settlement interface | Finality of transactions; treated as the most protected function |
| Communication links | Connectivity between components; may degrade intermittently |
| Monitoring and logging | Source of all observations available to the core |

**Trust boundaries:** external clients to gateway; gateway to internal services; internal services to external counterparties; monitoring to the defense core (read-only). The core receives observations only through the domain adapter.

## 4. Assets and properties to protect
Transaction integrity; service availability; authentication integrity; confidentiality of credentials and account data (represented only by synthetic identifiers); auditability of decisions.

## 5. Scenario families (initial)
All scenarios are synthetic, seeded and isolated.

**Security-relevant**
- S1: slow, distributed credential-stuffing against the authentication service, spread over time and sources to stay below per-event thresholds.
- S2: S1 combined with intermittent communication failures that mask or distort part of the evidence.
- S3: unusual sequence of individually authorized operations across components.

**Matched benign controls (deceptive by design)**
- B1: misconfiguration burst producing repeated authentication failures.
- B2: legitimate load spike (for example a payroll or sales peak).
- B3: scheduled maintenance with transient errors and restarts.
- B4: communication interruption without malicious activity.

**Neutral and stateless-favorable cases (to avoid built-in bias toward contextual detection)**
- N1: normal operation.
- N2: high-intensity single-event attack that a stateless rule should detect.

## 6. Observations available to the core
Normalized events carrying: domain_id, run_id, event_id, asset_id, event-time step, event type, outcome, source identifier class, and an observation-quality indicator. Ground-truth labels (scenario identity, attack stage, benign cause) are **never** visible to the online core and exist only for evaluation.

## 7. Candidate defensive actions (advisory only)
1. Continue monitoring.
2. Notify an operator.
3. Request additional verification (step-up) for affected sessions.
4. Recommend rate limiting or restricting selected operation types.
5. Recommend isolating a non-critical component.

Higher-numbered actions are more disruptive and, in general, less reversible. No action is executed by the framework; recommendations require human authorization.

## 8. Hard constraints (proposed; to be reviewed)
Hard constraints are feasibility conditions enforced by the independent safety gate. They are not costs to be traded off against benefit.
- HC-1: no recommendation may target the settlement interface for isolation or restriction without explicit human authorization.
- HC-2: no recommendation that would drop, alter or silently delay in-flight transactions.
- HC-3: restrictive actions require sufficient observation quality; with missing or untrusted context the outcome is monitoring plus a review signal.
- HC-4: restrictive actions require human authorization in this research phase.
- HC-5: an unknown action, unknown asset or missing policy is vetoed (fail closed).
- HC-6: every recommendation records contributing event IDs, rule and policy versions, and the reason for any veto.

## 9. Evaluation interface
Metrics, baselines and statistical design are defined in the preregistered H1 protocol, not here. This document fixes only what the generator must provide: scenario labels, matched benign controls, per-event ground truth held out from the core, seeds, and fixture hashes.

## 10. Assumptions and limitations
- The model is abstract and synthetic; scenarios authored by the project may favor contextual detection by construction (see the threats to validity in `ROADMAP.md`).
- Operational loss functions are approximations.
- Results will not establish effectiveness on real payment infrastructure.
- No real financial data, credentials or institution-specific configurations may be used or published.

## 11. Acceptance criteria for this specification
Reviewed and approved by the project owner; scenarios S1–S3, B1–B4 and N1–N2 unambiguously defined; hard constraints mapped to testable safety-gate cases; generator requirements consistent with the CORE-003 specification.
