# ACDRL Research Roadmap

**Version:** 0.2 — architecture-first revision (2026-10-19). Phases are evidence-gated, not deadlines.

| Phase | Main work | Exit evidence | Status |
| --- | --- | --- | --- |
| 0 — Governance and research setup | Repository, charter, logs, evidence standards | Documents versioned and reviewed | Documentation established |
| 1 — CORE-001 architecture | Domain-neutral modules, event/state/action contracts, safety policies, evaluation protocol, literature matrix | Reviewed architecture, test cases and interface schemas | **Current priority** |
| 2 — Minimum viable core | Event ingestion, rule detection, risk scoring, policy selection, safety veto, advisory response, audit trail | Unit tests, deterministic fixture tests, reproducible outputs | Planned |
| 3 — Spacecraft adapter and simulator | Map spacecraft telemetry/commands and safety constraints into core contracts; run ACDRL-SIM-001 | Validated simulation, baseline metrics and integration tests | Planned |
| 4 — Advanced decision research | Uncertainty, Monte Carlo trials, optimization and constrained RL where justified | Comparative experiments, safety/failure analysis | Planned |
| 5 — Financial adapter and transfer | Map synthetic payment events, transaction integrity and continuity constraints into core | Independent benchmarks, adaptation costs and failure cases | Planned |
| 6 — Synthesis and dissemination | Cross-domain analysis, replication, publications and technical demonstrations | Verifiable research outputs and external review where available | Planned |

## Immediate milestone — ACDRL-CORE-001
**Objective:** specify the reusable defense framework before building domain-specific simulation code.

**Deliverables:**
1. `research/core/CORE_ARCHITECTURE.md`: module responsibilities, flow and boundaries.
2. `research/core/INTERFACE_CONTRACTS.md`: common observation, context, alert, decision, action and evidence structures.
3. `research/protocols/ACDRL-CORE-001.md`: research questions, hypotheses, baselines, validation and transfer strategy.

**Exit gate:** contract schemas, threat/safety assumptions, failure behavior and deterministic core test fixtures reviewed. No algorithmic novelty or effectiveness claimed yet.

## Relationship to earlier work
The existing spacecraft documents `research/spacecraft/` and `research/protocols/ACDRL-SYS-001.md`, `ACDRL-SIM-001.md` are preserved as domain-one validation specifications. Their simulation implementation is deferred until the common core can accept synthetic events and issue safe advisory decisions.

## Research workflow
Problem → Literature → Gap assessment → Question → Hypothesis → Model → Design → Baseline → Experiment → Evaluation → Evidence → Decision.

## Release and communication gates
Do not publish performance claims without a recorded protocol, reproducible runs, baseline comparisons and limitations. Project documentation may be shared as an engineering milestone but not as a validated research finding.
