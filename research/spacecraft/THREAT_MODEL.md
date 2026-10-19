# ACDRL-SYS-001 — Initial Spacecraft Cybersecurity Threat Model

**Status:** Provisional, simulation-only (v0.1).  
**Method:** Asset and trust-boundary analysis with explicit separation of benign faults from adversarial scenarios.

## 1. Protected assets
- Authorized spacecraft command execution and command history.
- Integrity and timeliness of spacecraft telemetry.
- Safe spacecraft operating modes and resource limits.
- Availability of mission-control and ground-station communications.
- Audit logs, scenario labels, and experiment reproducibility.

## 2. Trust boundaries
| Boundary | Security concern | Candidate model control |
| --- | --- | --- |
| Operator → mission control | Operator impersonation / misuse | Role-based authorization |
| Mission control → ground station | Command origin and integrity | Authenticated requests and logs |
| Ground station → spacecraft | Replay, alteration, loss and delay | Freshness checks, validation, bounded queues |
| Spacecraft commands → state | Unsafe state transition | Command allowlist and invariant checks |
| System events → defense observer | Missing, delayed or misleading evidence | Event provenance and quality indicators |
| Defense observer → response authority | Harmful automatic action | Advisory-only phase, policy gate for later phases |

## 3. Scenario taxonomy
### Normal operations
- Routine telemetry production and authorized commands during a simulated contact window.
- Expected mode transitions and ordinary link variability.

### Benign faults (not attacks)
- Temporary packet loss, increased latency, contact interruption.
- Sensor drift or outlier, battery discharge, or a simulated component warning.
- Delayed legitimate command due to ground-station queue congestion.

### Adversarial scenarios (synthetic and isolated)
- **Unauthorized command attempt:** invalid actor or insufficient role; must not change spacecraft state.
- **Command replay:** repeated previously accepted command with stale sequence/freshness metadata.
- **Telemetry integrity anomaly:** altered or inconsistent telemetry fields introduced within the simulator.
- **Resource-exhaustion pressure:** excessive synthetic message traffic causing queue pressure, without generating external network traffic.

These are high-level controlled experiment cases; no interaction with real spacecraft, ground stations, or third-party services is authorized or implied.

## 4. Adversary model and limits
A modeled adversary may influence selected *simulated* messages or queue load at explicitly designated injection points. It cannot alter the experiment's ground-truth labels, change the simulator code during a run, access the host operating system, or control real communications. Capabilities and knowledge must be specified per experiment.

## 5. Security and mission-safety goals
1. Prevent unauthorized state changes.
2. Detect suspicious behavior without conflating benign faults and attacks.
3. Preserve availability and safe operating envelopes under modeled stress.
4. Maintain traceable decisions and bounded response times.
5. Require human authorization before disruptive mitigation in early phases.

## 6. Risk evaluation framework
For each scenario record: targeted asset, prerequisite, injected variable, likelihood assumptions (if modeled), safety impact, observable evidence, expected control, and residual risk. Do not assign quantitative likelihood without a justified data source or clearly labeled simulation assumption.

## 7. Evaluation concerns
- **False positives:** legitimate faults classified as attacks.
- **False negatives:** synthetic attacks missed by detection.
- **Detection latency:** time between observable onset and alert.
- **Mission impact:** time outside operating constraints, service availability, dropped authorized commands.
- **Integrity:** proportion of unauthorized state changes (target zero by design).
- **Robustness:** behavior across seeds, fault intensities, and link conditions.

## 8. Open issues
- Review domain-specific spacecraft security guidance and relevant academic literature.
- Refine actor roles and message semantics.
- Distinguish simulator fault injection from genuine exploit feasibility.
- Document which assumptions cannot be generalized to actual missions.

**Related documents:** [System architecture](SYSTEM_ARCHITECTURE.md) · [Research protocol](../protocols/ACDRL-SYS-001.md).
