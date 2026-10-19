# ACDRL-SYS-002 — Mathematical Model for a Notional Spacecraft

**Version:** 0.1 | **Status:** Draft specification, not flight-validated | **Scope:** Isolated software simulation

## Purpose and fidelity
Specify a deterministic discrete-time plant with optional seeded disturbances. This is an educational/research abstraction, not a physically calibrated spacecraft model. Parameters and safety envelopes below are **illustrative test settings**, not spacecraft standards. All numerical values must be reviewed against literature before any physical realism claims.

## State, inputs and time
At step k, with delta_t = 1 simulated second:
- b[k]: battery state of charge (%), clipped to [0, 100].
- T[k]: representative temperature (degrees Celsius).
- e[k]: nonnegative pointing-error magnitude (degrees).
- q[k]: downlink queue occupancy (nonnegative integer messages).
- m[k]: operational mode in {NOMINAL, SAFE}.

Inputs:
- P_gen[k], P_load[k] in watts.
- Q_in[k] in watts; T_env[k] in degrees Celsius.
- a[k] in {0,1}: authorized attitude-correction request accepted by spacecraft.
- d[k] in degrees per step: bounded disturbance, sampled by seeded RNG when enabled.
- A[k] and S[k]: telemetry arrivals and service count (messages per step).

## Discrete-time transitions
**Battery:** with E_max in watt-hours and delta_t in seconds,

b[k+1] = clip(b[k] + 100 * (P_gen[k] - P_load[k]) * delta_t / (3600 * E_max), 0, 100).

The factor 3600 is necessary to convert watts × seconds to watt-hours.

**Temperature:** with effective heat capacity C_th in joules per kelvin and heat transfer coefficient h in watts per kelvin,

T[k+1] = T[k] + delta_t * (Q_in[k] - h * (T[k] - T_env[k])) / C_th.

A temperature difference in Celsius is numerically equivalent to a difference in kelvin.

**Pointing-error proxy:**

e[k+1] = max(0, e[k] - k_a * a[k] * delta_t + d[k]),

where k_a has units degrees/second. This is not rigid-body attitude dynamics; it is a scalar tracking proxy.

**Downlink queue:**

q[k+1] = max(0, min(Q_max, q[k] + A[k] - S[k])).

Any overflow beyond Q_max is counted as dropped messages, not silently discarded.

**Mode transitions:** a SAFE transition is triggered by an explicitly configured safety predicate; SAFE→NOMINAL requires an authorized recovery command and satisfied recovery criteria. SAFE is not assumed to guarantee physical recovery.

## Illustrative configuration for first smoke test
| Parameter | Initial test value | Units / comment |
| --- | --- | --- |
| delta_t | 1 | second |
| horizon | 3600 | steps (one simulated hour) |
| E_max | 100 | Wh, illustrative |
| b[0] | 80 | percent |
| P_gen | 12 | W, fixed baseline |
| P_load | 10 | W, fixed baseline |
| T[0] | 20 | degrees Celsius |
| T_env | 10 | degrees Celsius |
| Q_in | 5 | W |
| C_th | 1000 | J/K |
| h | 0.5 | W/K |
| e[0] | 2 | degrees |
| k_a | 0.01 | degrees/second when correction active |
| Q_max | 100 | messages |
| A[k] | 1 | message per step |
| S[k] | 1 | message per step in contact |

These values are selected for transparent, bounded software behavior; they do not model an actual spacecraft power, thermal, or attitude subsystem.

## Safety and command integrity
1. Unauthorized, malformed, stale or replayed commands cannot change plant state.
2. A command is applied only after authentication, authorization, freshness and parameter validation.
3. Each applied command records a unique ID, sequence number, accepted timestamp, actor and resulting state transition.
4. Proposed test thresholds: battery >= 20%; -10 <= T <= 50 degrees Celsius; e <= 10 degrees in NOMINAL mode. They are configurable, synthetic limits, not universal safe operating envelopes.
5. No automatic disruptive cyber countermeasure is enabled in this milestone.
6. A safety check records any threshold violation; clipping alone must not be used to hide physically invalid simulation behavior.

## Randomness, determinism and numeric checks
- Use a documented pseudorandom generator and fixed seed.
- Same source revision, configuration, seed and execution environment must produce identical canonical event outputs.
- Validate units, nonnegative queue, integer message counts, finite numeric values, battery bounds, and mode transition guards.
- Validate simple analytic cases (e.g., fixed net power yields a linear battery trajectory before clipping).
- Store actual simulation results only after code execution and test review.

## Out of scope
Orbital dynamics, true 3-axis attitude dynamics, RF waveform physics, CCSDS protocol fidelity, radiation, hardware-in-the-loop, and flight qualification.

## Next engineering gate
Approve telemetry/command schemas and the ACDRL-SIM-001 protocol before writing the first Python simulator.
