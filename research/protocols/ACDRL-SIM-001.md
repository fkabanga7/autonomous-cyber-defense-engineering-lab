# ACDRL-SIM-001 — Nominal Spacecraft Operations Validation Protocol

**Version:** 0.1 | **Status:** Draft, not executed  
**Parent:** ACDRL-SYS-001 / ACDRL-SYS-002  
**Environment:** Isolated, synthetic, discrete-time spacecraft and ground-station simulator

## Research question
Can the initial simulator execute authorized commands, evolve state consistently with documented equations, produce well-formed telemetry, and reproduce identical outputs for a fixed configuration and seed under nominal conditions?

This is a **software validation experiment**, not proof of realistic spacecraft operation or AI performance.

## Hypotheses
- H1: all accepted commands pass schema, authorization, freshness and safety checks; unauthorized commands cause zero state changes.
- H2: fixed code, configuration and seed yield identical canonical outputs.
- H3: numerical state trajectories match independently computed expected values within stated floating-point tolerances when disturbances are disabled.
- H4: no safety invariant is violated in the nominal reference configuration.

## Initial configuration
- Duration: 3600 steps, delta_t = 1 simulated second.
- Single simulated spacecraft and ground station, contact initially available.
- Use the illustrative parameter set in [MATHEMATICAL_MODEL.md](../spacecraft/MATHEMATICAL_MODEL.md).
- Seed: 42 for the first reference run; later vary seeds for stochastic scenarios.
- Telemetry: once per simulation step.
- Command test cases: one authorized attitude-correction toggle, one authorized safe-mode request, one authorized recovery (only if recovery conditions are satisfied), and deliberately rejected invalid/replayed commands in isolated tests.
- Disturbances: disabled in the nominal reference run.
- Link packet loss: zero in the nominal reference run.

## Protocol steps
1. Record source commit, OS, Python version, dependency versions, configuration and seed.
2. Run static validation of configuration and telemetry/command schemas.
3. Execute unit tests of each transition equation against independently calculated expected values.
4. Run 3600 nominal steps with deterministic event ordering.
5. Verify message sequencing, event logging and no duplicate applied command IDs.
6. Verify battery, temperature, attitude proxy, queue and mode invariants.
7. Repeat the reference run with the same seed and compare canonical output hashes.
8. Run rejected-command tests separately, confirming no unauthorized state mutation.
9. Record failures and revise the model before introducing fault or adversarial scenarios.

## Evaluation metrics
- Number of schema violations and invalid numeric values.
- Number of unauthorized state changes (target 0).
- Number of unexpected safety-invariant violations (target 0).
- Absolute/relative error against independent reference calculations (tolerance declared before execution).
- Run-to-run canonical output equality.
- Number of lost or duplicated messages under the zero-loss reference configuration.
- Simulated elapsed time and runtime overhead.

## Acceptance criteria
- All defined unit tests pass.
- Every generated telemetry record conforms to the schema.
- Fixed-seed repeatability succeeds.
- No unauthorized command alters spacecraft state.
- No unexpected invariant violation occurs under nominal settings.
- Any observed deviation is investigated and recorded rather than concealed.

## Required evidence
- Run ID, date, Git commit SHA and protocol version.
- Configuration and environment manifest.
- Test report, JSONL telemetry/events and SHA-256 hashes.
- Reproducible run instructions and analysis scripts.
- Results summary including deviations and limitations.

## Publication policy
A passing nominal simulation supports an engineering milestone update, not a scientific claim of autonomous cyber-defense effectiveness. Publish figures or demonstrations only after reviewing their provenance and security.

## Deferred work
Fault injection, synthetic adversarial scenarios, anomaly detection, statistical comparisons, Monte Carlo experiments, reinforcement learning and cross-domain financial transfer all require later protocols.

**Related:** [Telemetry schema](../spacecraft/TELEMETRY_SCHEMA.md) · [Mathematical model](../spacecraft/MATHEMATICAL_MODEL.md).
