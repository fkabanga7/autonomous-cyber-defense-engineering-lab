# ACDRL-STEALTH-001 — Contextual Detection and Safety-Constrained Decisions

**Version:** 0.1 | **Status:** Proposed research protocol; no experiments executed.

## Research question
Can temporal context and explicit observation uncertainty improve detection of subtle anomalies in synthetic mission-critical systems compared with stateless rules, while limiting unnecessary defensive interventions?

## Scenario families
- Sparse, low-intensity deviations spread across time.
- Unusual sequences of otherwise authorized operations.
- Cross-component access patterns inconsistent with expected workflows.
- Inconsistent telemetry and state transitions.
- Missing monitoring data or degraded data provenance.
- Matched benign controls: maintenance, clock drift, sensor failure, workload changes, and communication interruptions.

All scenarios use isolated simulations, synthetic events and authorized research data. No operational access, live system changes or exploitation is included.

## Hypotheses
H1: Contextual window features increase sequence-level recall at a fixed false-alarm budget relative to the CORE-002 stateless baseline.
H2: Explicit missingness and uncertainty indicators support more reliable abstention and human-review recommendations than unqualified heuristic scores.
H3: An independent safety constraint reduces inappropriate operational recommendations compared with an unconstrained decision baseline.
H4: Reusable interfaces can support both spacecraft and financial simulation, but effectiveness must be independently evaluated in each domain.

## Experimental plan
1. Freeze baseline source revision, schemas, policy versions and test fixtures.
2. Build labeled synthetic sequences with independent random seeds and benign matched controls.
3. Compare stateless rules, temporal rules, statistical sequence models, and uncertainty-aware approaches if justified.
4. Separate tuning and evaluation by sequence families; keep scenario labels inaccessible to the online decision pipeline.
5. Measure performance and failure cases across multiple seeds, then repeat separately in both domains.
6. Retain advisory-only output and independent safety veto throughout.

## Metrics
Sequence recall, precision, false alarms per observation hour, detection delay, coverage/abstention, decision latency, operational-impact proxy, and safety-veto correctness. Use calibration error or Brier score only when probabilities have actually been calibrated.

## Decision formulation
Maintain a belief about plausible system conditions from observations available so far. Choose a permitted advisory decision minimizing expected security loss, operational disruption and response cost. Candidate decisions: NO_ACTION, ALERT_OPERATOR, REQUEST_HUMAN_REVIEW, and a proposed INCREASE_OBSERVATION advisory. Any new decision requires an explicit policy and safety review.

Initial experiments may use deterministic or heuristic uncertainty categories. Do not call them probabilities. A probabilistic decision model or constrained reinforcement learning requires separate validation of assumptions and baselines.

## Evidence and exit gates
Preserve source commit, configuration, scenario generator, seed, input/output hashes, exact test results and limitations. Require benign/adversarial controls, reproducible baseline comparison, leakage checks and safety-veto tests before reporting results.

**No scientific performance results are claimed by this document.**
