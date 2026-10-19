# ACDRL-SYS-001 — Spacecraft–Ground Segment System Architecture

**Status:** Provisional research design (v0.1)  
**Scope:** One simulated spacecraft, one ground station, one mission-control service, and an observational cyber-defense subsystem.  
**Validation status:** Conceptual only; no simulator or empirical results exist yet.

## 1. Research purpose
Define an intentionally simplified, reproducible cyber-physical system in which normal operation, benign faults, and cyber-relevant anomalies can be distinguished and evaluated. The model is not a flight-qualified spacecraft design or an operational mission architecture.

## 2. Logical components
1. **Spacecraft simulator:** evolves mission state, executes allowed commands, produces telemetry, and enforces simplified safety invariants.
2. **Communication link simulator:** transports uplink commands and downlink telemetry, modeling latency, jitter, packet loss, contact windows, and bounded reordering.
3. **Ground station:** accepts commands from mission control, applies authentication/authorization checks in the model, queues uplinks, receives downlinks, and logs events.
4. **Mission control:** creates approved command requests, displays mission state, and tracks operational decisions.
5. **Cyber-defense subsystem:** initially observes events and raises alerts. Any later countermeasure must be explicitly authorized by a policy and constrained by mission safety; no autonomous action is assumed in the first experiment.
6. **Experiment controller:** injects labeled, controlled fault/anomaly scenarios, records seeds and configuration, and exports evidence.

## 3. Conceptual flows
- **Uplink:** mission control → ground station authorization/validation → link → spacecraft command validator → state transition.
- **Downlink:** spacecraft telemetry/event generation → link → ground station → mission control and defense observer.
- **Evidence:** all simulated components → structured event collector → experiment artifacts and metrics.
- The first version models **logical messages**, not real radio-frequency modulation or a flight protocol.

## 4. Initial state and observables (illustrative)
| Category | Variables / events | Initial interpretation |
| --- | --- | --- |
| Power | battery state of charge, generation, load | Bounded resource state |
| Thermal | representative component temperature | Operating-envelope constraint |
| Attitude | simplified pointing error / mode | Mission availability proxy |
| Communications | contact status, delay, loss, queue length | Channel quality and access |
| Command integrity | command ID, origin, authorization result, sequence number | Command provenance and policy |
| Operations | mission mode, watchdog events, state transitions | Safety and continuity |
| Cyber observation | alerts, scores, decision timestamps | Detector outputs, not ground truth |

Units, valid ranges, update intervals, and transition equations must be specified and justified in a later simulator specification before implementation.

## 5. Trust boundaries and assumptions
- Mission control ↔ ground station (operator identity and command authorization).
- Ground station ↔ communication link ↔ spacecraft (integrity, authenticity, freshness and availability).
- Spacecraft command handler ↔ simulated subsystems (state-transition safety).
- Observer ↔ response controller (advisory output versus permitted intervention).
- Experiment controller holds *synthetic* ground-truth labels, kept logically separate from detection features to avoid label leakage.

**Assumptions:** discrete-time simulator, synthetic telemetry, bounded state transitions, one spacecraft, no real uplink or downlink, no live infrastructure access. Link behavior and attacker capabilities are intentionally limited and explicitly documented.

## 6. Safety invariants (to be formalized)
- Unauthenticated or unauthorized commands never alter spacecraft state.
- Commands violating defined safety envelopes are rejected or require operator review.
- Cyber-defense actions must not disable essential mission functions without an explicitly modeled safety justification and approval.
- Every accepted command and state transition is auditable.
- Detection alerts alone do not trigger automatic disruptive action in the first study.

## 7. Proposed simulator modules (not yet implemented)
```text
src/acdrl/
  spacecraft.py
  link.py
  ground_station.py
  mission_control.py
  events.py
  scenarios.py
  metrics.py
tests/
experiments/
```
This is a future layout proposal, not a statement that these files exist.

## 8. Fidelity limitations
The first simulator will not represent orbital mechanics, radiation effects, RF waveforms, actual spacecraft bus protocols, hardware-in-the-loop behavior, or real mission operations. These omissions limit external validity and must be disclosed with every result.

## 9. Next design decisions
- Select a notional mission profile and a minimum viable operating mode.
- Define state-transition equations and units.
- Specify message schema, command whitelist, and threat scenarios.
- Select reproducibility conventions and literature references before claiming scientific gaps.

**Related documents:** [Threat model](THREAT_MODEL.md) · [Research protocol](../protocols/ACDRL-SYS-001.md).
