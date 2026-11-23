# ACDRL Research Roadmap

**Version:** 0.4 — financial-first alignment (2026-11-23). Phases are evidence-gated, not deadlines.

The core is domain-independent. Critical financial payment systems are the first validation testbed; spacecraft and ground-segment systems are evaluated afterwards as an independent transfer study.

| Phase | Main work | Exit evidence | Status |
| --- | --- | --- | --- |
| 0 — Governance and alignment | Repository, charter, logs, evidence standards; financial-first alignment; Master Framework; ACDRL-FIN-001 | Documents versioned and reviewed | In progress |
| 1 — CORE-001 architecture | Domain-neutral modules, event/state/action contracts, safety policies, evaluation protocol | Reviewed architecture, test cases and interface schemas | Documented |
| 2 — CORE-002 minimum viable core | Event ingestion, rule detection, risk scoring, safety veto and audit | 11/11 local unit tests passed on 2026-10-20; scope-limited evidence registered | Initial unit tests passed |
| 3a — Literature review and gap assessment | Literature matrix covering detection, SOAR, autonomous cyber defense, safe and constrained decision-making, runtime assurance | Reviewed matrix and positioning of claimed contributions | Planned; must complete before Phase 5 |
| 3b — CORE-003 temporal context | Bounded event history, configurable rules, provenance, deduplication, deterministic sequence tests | New unit tests and CORE-002 comparison | **Next implementation** |
| 3c — Minimal financial testbed | Seeded synthetic generator; two or three scenarios; deceptive benign cases; ground truth held out from the online core (built in parallel with 3b under ACDRL-FIN-001) | Deterministic replay, fixture hashes, documented scenario labels | Planned |
| 4 — First experiment (H1) | Preregistered comparison of CORE-002 (stateless) and CORE-003 (contextual) at a fixed false-alarm budget; thresholds tuned on validation seeds, test seeds frozen; at least 30 runs per scenario with confidence intervals; recall, false alarms per 1,000 benign hours, detection delay | Preregistered protocol, frozen seeds, reproducible results, failure analysis | Planned |
| 5 — CORE-004 and CORE-005 | Missingness, observation quality and abstention; safety-constrained advisory selection with human review | Calibration and coverage evaluation; policy comparisons and veto tests | Planned |
| 6 — Experiments H2 and H3 | Controlled comparison of uncertainty-aware and constrained policies against conventional baselines | Preregistered evaluations, operational-loss estimates, safety compliance | Planned |
| 7 — Spacecraft transfer (H4) | Spacecraft adapter; ACDRL-SIM-001 simulator validation; independent transfer evaluation | Validated simulation, adaptation costs, failure cases | Planned; last |
| 8 — Synthesis and dissemination | Three articles (H1; H2 and H3; H4), replication package, technical demonstrations | Verifiable research outputs and external review where available | Planned |

## Immediate milestone — ACDRL-CORE-003 with the minimal financial testbed
**Objective:** implement and test domain-independent temporal context, deterministic sequence detection, configuration-driven policies and fail-closed handling, together with the minimal financial event generator needed to evaluate it.

**Deliverables:**
1. Implementation of the components in `research/core/ACDRL-CORE-003_SPECIFICATION.md`.
2. `research/protocols/ACDRL-FIN-001.md`: financial system boundary, threat scenarios, observations, defensive actions and hard constraints.
3. A seeded synthetic financial event generator with held-out ground truth.

**Exit gate:** deterministic sequence tests, explicit failure semantics, safety gate checks, exact source revision and fixture hashes, and comparison with CORE-002. No anomaly-detection performance claims until the preregistered H1 experiment.

## Threats to validity to address in Phase 4
Scenarios authored by the project favor contextual detection by construction. The H1 design therefore includes scenarios where stateless rules should suffice, adversarial or degraded-context cases, and, where legally usable, a control on real public authentication data (for example the LANL cyber-security dataset; to be verified).

## Relationship to earlier work
The spacecraft documents in `research/spacecraft/` and `research/protocols/ACDRL-SYS-001.md`, `ACDRL-SIM-001.md` are preserved unchanged as provisional specifications for the second validation domain (Phase 7). `ACDRL-STEALTH-001` remains the general contextual-detection protocol; its financial instantiation is defined through ACDRL-FIN-001.

## Research workflow
Problem → Literature → Gap assessment → Question → Hypothesis → Model → Design → Baseline → Experiment → Evaluation → Evidence → Decision.

## Release and communication gates
Do not publish performance claims without a recorded protocol, reproducible runs, baseline comparisons and limitations. Project documentation may be shared as an engineering milestone but not as a validated research finding.
