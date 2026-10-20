# ACDRL Experiment Registry

No scientific experiments have been completed yet. This registry distinguishes planned work from validated findings.

| Experiment ID | Question | Protocol | Status | Evidence | Conclusion |
| --- | --- | --- | --- | --- | --- |
| ACDRL-SYS-001 | What spacecraft/ground-segment system boundary and safety constraints should the first simulator represent? | To be drafted | Planned | None | Not evaluated |

| ACDRL-CORE-002-UT-001 | Does the initial advisory-only core pass its deterministic unit tests on the owner's Mac? | `PYTHONPATH=src python -m unittest discover -s tests -v` (engineering test procedure; not a scientific experiment protocol) | **Engineering unit tests: passed 2026-10-20** | Owner-provided terminal screenshot (not archived in repo); 11/11 `ok`, `OK`; baseline GitHub revision `8c12e886b802cc046e8eb1aaaafa8726c594ac89` (local HEAD at execution unconfirmed) | Selected unit tests passed; no scientific or operational effectiveness established |

## Required experiment record
- Experiment ID and owner
- Literature references and research gap assessment
- Research question and falsifiable hypothesis
- System boundary and threat model
- Independent/dependent variables and safety constraints
- Dataset/simulator version, provenance and integrity checks
- Baseline methods and justification
- Environment, dependency versions, configuration, random seeds
- Evaluation metrics and statistical methods
- Git commit and reproducible execution instructions
- Results, negative results, limitations, and decision

## Status vocabulary
**Planned → Protocol approved → Implementing → Evaluating → Reproduced → Reported**, or **Blocked / Superseded** with an explanation.

Never label a learning exercise or simulation output as a novel scientific contribution without substantiation.
