# ACDRL-CORE-002 — Preliminary Unit Verification Report

**Verification identifier:** `ACDRL-CORE-002-UT-002`  
**Execution date:** 2026-10-22  
**Status:** Owner-executed; terminal output reviewed; 11/11 tests passed  
**Evidence classification:** Local unit-test verification, not operational validation

## 1. Objective

Reproduce the CORE-002 unit-test result and capture the source revision, Python interpreter version, working-tree state, and test transcript so the engineering baseline can be traced to a specific repository state.

## 2. Environment and source revision

| Property | Recorded value | Basis |
|---|---|---|
| Host | MacBook Air, macOS / zsh | User-provided terminal screenshot |
| Python interpreter | Python 3.14.6 | `python --version` in screenshot |
| Python environment | `.venv` active | Shell prompt in screenshot |
| Git HEAD | `8c12e886b802cc046e8eb1aaaafa8726c594ac89` | `git rev-parse HEAD` in screenshot |
| Working tree | No changes reported | `git status --short` yielded no visible entries |
| Test runner | `unittest` discovery | Command in screenshot |
| Test-output file | `CORE-002-test-output.txt` | Shell redirection shown; file content not independently retrieved or archived here |

The reported test output was captured with:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v 2>&1 | tee CORE-002-test-output.txt
```

This document relies on the owner's displayed terminal evidence. It does not assert that the author of this report independently executed the tests.

## 3. Recorded tests

| Test | Result |
|---|---|
| `test_detection.PipelineTests.test_denial_alert` | PASS |
| `test_detection.PipelineTests.test_deterministic` | PASS |
| `test_detection.PipelineTests.test_normal_no_action` | PASS |
| `test_detection.PipelineTests.test_two_domains_same_pipeline` | PASS |
| `test_ingestion.IngestionTests.test_bool_step_rejected` | PASS |
| `test_ingestion.IngestionTests.test_invalid_schema` | PASS |
| `test_ingestion.IngestionTests.test_missing_field` | PASS |
| `test_ingestion.IngestionTests.test_valid` | PASS |
| `test_safety.SafetyTests.test_advisory_allowed_but_not_executed` | PASS |
| `test_safety.SafetyTests.test_disruptive_action_vetoed` | PASS |
| `test_safety.SafetyTests.test_missing_policy_fails_closed` | PASS |

**Terminal summary:** `Ran 11 tests in 0.001s` followed by `OK` for the captured `tee` invocation. A preceding run in the same screenshot also showed 11 tests and `OK` (reported `0.000s`). No failures or errors were displayed.

## 4. Coverage interpretation

The tests check selected schema constraints, the current denial-event detection rule, basic advisory decision mapping, output determinism for repeated identical input, processing with synthetic `spacecraft` and `financial` domain identifiers, and two safety veto conditions.

The domain-label test does **not** verify actual spacecraft or payment-system interoperability. The fixed detection score is not empirically calibrated. The reported sub-millisecond timing is a runner observation and should **not** be interpreted as a throughput or latency benchmark.

## 5. Evidence provenance and limitations

- `UT-002` is separate from the earlier October 20, 2026 run (`UT-001`); do not overwrite the earlier historical entry.
- The October 22 screenshot includes the Git HEAD, interpreter version, empty `git status --short` output, test command, individual passing tests, and summary.
- The shell command creates `CORE-002-test-output.txt` in the repository working directory. The screenshot alone does not establish that this file was committed, hashed, or uploaded. Note also that it would ordinarily be an untracked file after the command; the clean status displayed **before** the `tee` invocation does not prove the working tree remained clean afterward.
- The complete transcript and screenshot should be archived with explicit relative paths and SHA-256 hashes before declaring the evidence package complete.
- No external laboratory, operational telemetry, penetration testing, attack detection benchmarks, or live intervention tests were conducted.

## 6. Suggested archival procedure (not yet performed)

From the repository root, preserve the existing transcript, record its hash, and capture a final working-tree status:

```bash
shasum -a 256 CORE-002-test-output.txt
git status --short
```

Proposed evidence location (subject to repository review and user approval): `evidence/CORE-002/UT-002/`. Store the test transcript, screenshot, a small environment manifest, and checksums. Avoid adding private host details or secrets. Do not modify or commit any files until reviewed.

## 7. Conclusion

**Result:** PASS — eleven owner-executed local unit tests passed against the displayed baseline revision.  
**Assurance level:** Preliminary functional verification only.  
**Outstanding evidence task:** Archive and hash the actual terminal transcript and screenshot.
