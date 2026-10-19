# ACDRL Research Roadmap

The phases below are **evidence-gated**, not calendar commitments.

| Phase | Objective | Exit criteria | Status |
| --- | --- | --- | --- |
| 0 — Infrastructure | Repository, charter, documentation, environment plan | Foundational records reviewed; first protocol drafted | In progress |
| 1 — Spacecraft foundations | Ground/space architecture, interfaces, constraints, threat model, literature | Traceable architecture, safety assumptions, initial research question | Planned |
| 2 — Spacecraft simulation | Isolated environment, normal operation, controlled anomalies, rule baselines | Repeatable simulation, verified scenarios, baseline metrics | Planned |
| 3 — AI detection | ML/anomaly methods and evaluation under realistic constraints | Baseline comparisons, uncertainty and robustness analysis | Planned |
| 4 — Adaptive defense | MDP formulation, decision baselines, Monte Carlo and constrained RL | Safety-aware evaluation and documented failure modes | Planned |
| 5 — Financial transfer | Simulated payment infrastructure and domain adaptation | Independent comparison of transferable and non-transferable methods | Planned |

## First milestone: ACDRL-SETUP-001
**Goal:** Create research documentation and confirm GitHub structure.

**Next actions:** review charter; select spacecraft system boundary; build a literature matrix; write protocol ACDRL-SYS-001; specify the local Python environment.

**Exit evidence:** reviewed project documents, initial commit references, and approved first research protocol.

## Research workflow
Problem → Literature → Gap assessment → Question → Hypothesis → Model → Design → Baseline → Experiment → Evaluation → Evidence → Decision.

## Decision gates
Do not advance solely because code executes. Require documented objectives, appropriate comparison, reproducibility, explicit limitations, and a justified next experiment.

## Publication strategy
Publications emerge from verified findings. A possible trajectory is spacecraft threat detection → safe adaptive defense → transfer to financial infrastructure. Exact paper titles and novelty claims remain provisional until literature review and results.
