# ACDRL-SYS-002 — Telemetry, Command and Event Schemas

**Version:** 0.1 | **Status:** Proposed interfaces, not implemented

## Design principles
All messages are synthetic, JSON-compatible and versioned. Timestamps use integer simulation steps; optional wall-clock timestamps are for execution metadata only. Command authorization decisions are not inferred from the command's self-declared actor field. Separate ground-truth scenario metadata from detector-observable telemetry.

## Telemetry message
Example (illustrative, not actual simulator output):
```json
{
  "schema_version": "0.1",
  "message_type": "telemetry",
  "spacecraft_id": "SIM-SC-001",
  "step": 0,
  "mode": "NOMINAL",
  "battery_soc_pct": 80.0,
  "temperature_c": 20.0,
  "pointing_error_deg": 2.0,
  "downlink_queue_messages": 0,
  "contact_available": true,
  "sequence": 0
}
```
Required fields: schema_version (string), message_type (constant), spacecraft_id (string), step (integer >= 0), mode (enum), battery_soc_pct (finite number in [0,100]), temperature_c (finite number), pointing_error_deg (finite nonnegative number), downlink_queue_messages (integer >= 0), contact_available (boolean), sequence (integer >= 0).

## Command request
Example (illustrative):
```json
{
  "schema_version": "0.1",
  "message_type": "command",
  "command_id": "cmd-000001",
  "spacecraft_id": "SIM-SC-001",
  "actor_id": "operator-1",
  "command": "SET_ATTITUDE_CORRECTION",
  "parameters": {"enabled": true},
  "sequence": 1,
  "issued_step": 10,
  "expires_step": 20
}
```
Initial allowlist: SET_ATTITUDE_CORRECTION, REQUEST_SAFE_MODE, REQUEST_NOMINAL_MODE. Define a per-role permission table in implementation. REQUEST_NOMINAL_MODE requires safe recovery criteria. Unknown commands and unknown parameter keys are rejected.

### Validation order
1. Parse and validate schema and numeric types.
2. Validate trusted actor authentication/authorization context supplied by the ground station.
3. Check command allowlist and parameter bounds.
4. Verify expiry, freshness and monotonic per-actor sequence / replay policy.
5. Check safety preconditions.
6. Apply at most once, atomically, and append audit event.

The example is **not** a cryptographic authentication protocol. A real mission would need a separately validated security design.

## Event record
```json
{
  "schema_version": "0.1",
  "event_id": "evt-000001",
  "step": 10,
  "component": "spacecraft",
  "event_type": "COMMAND_REJECTED",
  "command_id": "cmd-000001",
  "reason_code": "UNAUTHORIZED"
}
```
Other candidate event types: TELEMETRY_EMITTED, COMMAND_ACCEPTED, MODE_CHANGED, LINK_LOSS, QUEUE_OVERFLOW, SAFETY_VIOLATION, DETECTOR_ALERT. Reasons are enumerated rather than free-form secrets.

## Ground-truth scenario metadata (restricted to experiment evaluator)
```json
{
  "run_id": "ACDRL-SIM-001-run-001",
  "seed": 42,
  "scenario_class": "normal",
  "injection_intervals": [],
  "protocol_version": "0.1"
}
```
Never feed scenario_class, injection_intervals or future outcome fields into detectors.

## Data integrity and reproducibility
- Write newline-delimited JSON (JSONL) for events and telemetry.
- Canonicalize output for deterministic comparisons (stable key order and float serialization policy).
- Reject NaN, Infinity, invalid units and duplicate message IDs.
- Record configuration hash, code commit, dependency versions and seed in the run manifest.
- Do not commit raw private data, credentials or unreviewed large output.

## Planned schema tests
Missing required field; invalid mode; battery outside bounds; nonfinite temperature; negative queue; duplicate command ID; replayed sequence; expired command; unauthorized actor; forbidden state transition; scenario label leakage.

## Open design decisions
Specify per-command authorization matrix, replay-window policy, event-ordering rules, and telemetry emission cadence before implementation.
