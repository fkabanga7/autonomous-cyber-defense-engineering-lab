# ACDRL Research Log

Chronological, append-only record of significant project decisions, milestones, obstacles, and next actions.

## 2026-10-19 — ACDRL-SETUP-001 initiated
**Decision:** Use a formal research lifecycle and spacecraft-first, finance-second application sequence.

**Rationale:** A shared methodological core permits rigorous comparison of AI cyber defense across mission-critical environments without presuming cross-domain transfer.

**Repository audit:** GitHub repository located; initially public and empty, default branch `main`.

**Actions approved:** Create seven foundational text files.

**Research results:** None. No experiments have been conducted as part of this milestone.

**Next:** Review charter and roadmap; establish system boundary and literature-review protocol for ACDRL-SYS-001.


## 2026-10-19 — Architecture-first decision; ACDRL-CORE-001 authorized
**Decision:** Make the reusable, domain-independent cyber-defense framework the primary research and engineering product. Spacecraft and financial infrastructure will be separate validation domains.

**Reason:** Building a spacecraft simulator first could overfit the defense design to a single domain. Explicit interfaces, safety contracts and shared evaluation logic should be specified before substantial domain-specific implementation.

**Impact:** Revise the charter and roadmap; preserve existing spacecraft research documents without alteration; add core architecture, interface contracts and research protocol.

**Research results:** None. This is an architectural decision and documentation milestone, not empirical validation.

**Next:** Review common event/state/action schemas, develop deterministic advisory-only test fixtures, then plan the first Python implementation.

## 2026-10-20 — ACDRL-CORE-002 local unit-test validation
**Question:** Does the initial advisory-only core pass its first deterministic unit-test suite on the project owner's Mac?

**Evidence:** Owner-provided VS Code terminal screenshot, October 20, 2026, showing `PYTHONPATH=src python -m unittest discover -s tests -v`, eleven tests marked `ok`, `Ran 11 tests in 0.000s`, and `OK`. Screenshot was reviewed in the conversation; it has **not** been uploaded to the repository.

**Environment reported:** Apple Silicon Mac (arm64); Python 3.14.6; activated project-local `.venv`; local path `/Users/diamant/Downloads/GitHub/autonomous-cyber-defense-engineering-lab`.

**Source revision:** `8c12e886b802cc046e8eb1aaaafa8726c594ac89` (GitHub `main` at the time the initial core implementation was committed). The screenshot shows the local branch tracking `origin/main` with a clean working tree before the run; an explicit `git rev-parse HEAD` at test time was not captured, so exact local test-run SHA is **not independently confirmed**.

**Result:** 11/11 existing unit tests passed, zero reported failures or errors. The tests cover selected input-validation cases, rule-based advisory decisions, deterministic output for identical fixtures, two synthetic domain IDs, and safety vetoes.

**Limitations:** Unit-test pass only; no measured detection accuracy, no production integration, no validated spacecraft/financial transfer, no external reproduction, and no autonomous operational actuation. Existing tests do not establish complete schema conformance or comprehensive security assurance.

**Next:** Preserve the result as an engineering baseline; collect `git rev-parse HEAD` and a machine-readable test log for stronger reproducibility; design CORE-003 stateful detection and policy controls.

## Log template
### YYYY-MM-DD — Milestone ID
- **Question or decision:**
- **Evidence consulted:**
- **Action taken:**
- **Result / limitation:**
- **Git reference:**
- **Next action:**
