# ACDRL Research Roadmap

**Version:** 0.3 — temporal context and uncertainty research plan (2026-10-22). Phases are evidence-gated, not deadlines.

| Phase | Main work | Exit evidence | Status |
| --- | --- | --- | --- |
| 0 — Governance and research setup | Repository, charter, logs, evidence standards | Documents versioned and reviewed | Documentation established |
| 1 — CORE-001 architecture | Domain-neutral modules, event/state/action contracts, safety policies, evaluation protocol, literature matrix | Reviewed architecture, test cases and interface schemas | Documented |
| 2 — CORE-002 minimum viable core | Event ingestion, rule detection, risk scoring, safety veto and audit | 11/11 local unit tests passed on 2026-10-20; scope-limited evidence registered | Initial unit tests passed |
| 3 — CORE-003 temporal context | Bounded event history, configurable rules, provenance, deduplication, deterministic sequence tests | New unit tests and CORE-002 comparison | **Next implementation** |\n| 4 — CORE-004 uncertainty | Missingness, observation quality, abstention and calibrated probabilities only when supported | Calibration and coverage evaluation | Planned |\n| 5 — CORE-005 safe decisions | Safety-constrained advisory selection under uncertainty and human review | Policy comparisons, veto tests and operational-loss evaluation | Planned |\n| 6 — CORE-006 controlled comparison | Synthetic anomaly sequences, Monte Carlo and reproducible baselines | Preregistered ACDRL-STEALTH-001 evaluations | Planned |\n| 7 — Spacecraft adapter and simulator | Map spacecraft telemetry/commands and safety constraints into core contracts; run ACDRL-SIM-001 | Validated simulation, baseline metrics and integration tests | Planned |
| 4 — Advanced decision research | Uncertainty, Monte Carlo trials, optimization and constrained RL where justified | Comparative experiments, safety/failure analysis | Planned |
| 8 — Financial adapter and transfer | Map synthetic payment events, transaction integrity and continuity constraints into core | Independent benchmarks, adaptation costs and failure cases | Planned |
| 9 — Synthesis and dissemination | Cross-domain analysis, replication, publications and technical demonstrations | Verifiable research outputs and external review where available | Planned |

## Immediate milestone — ACDRL-CORE-003
**Objective:** implement and test domain-independent temporal context, deterministic sequence detection, configuration-driven policies and fail-closed handling.

**Deliverables:**
1. `research/core/CORE_ARCHITECTURE.md`: module responsibilities, flow and boundaries.
2. `research/core/INTERFACE_CONTRACTS.md`: common observation, context, alert, decision, action and evidence structures.
3. `research/protocols/ACDRL-CORE-001.md`: research questions, hypotheses, baselines, validation and transfer strategy.

**Exit gate:** deterministic sequence tests, explicit failure semantics, safety gate checks, exact source revision and comparison with CORE-002. No anomaly-detection performance claims until controlled experiments.

## Relationship to earlier work
The existing spacecraft documents `research/spacecraft/` and `research/protocols/ACDRL-SYS-001.md`, `ACDRL-SIM-001.md` are preserved as domain-one validation specifications. Their simulation implementation is deferred until the common core can accept synthetic events and issue safe advisory decisions.

## Research workflow
Problem → Literature → Gap assessment → Question → Hypothesis → Model → Design → Baseline → Experiment → Evaluation → Evidence → Decision.

## Release and communication gates
Do not publish performance claims without a recorded protocol, reproducible runs, baseline comparisons and limitations. Project documentation may be shared as an engineering milestone but not as a validated research finding.
