# Autonomous Cyber Defense Engineering Lab (ACDRL)

**Research mission:** Autonomous Cyber Defense and Resilience Engineering for Critical Financial Infrastructure and Spacecraft Systems.

ACDRL is an independent applied research and engineering initiative investigating how AI-supported detection and adaptive defensive decisions can protect mission-critical systems while respecting safety, availability, and operational constraints.

## Research sequence
The reusable, domain-independent defense core is the primary engineering product. Domains are validation environments, evaluated in this order:

1. **Critical financial payment systems (first testbed):** synthetic events and isolated simulations of authentication, transaction processing, communication and availability threats.
2. **Spacecraft and ground-segment systems (second domain):** independent evaluation of which methods transfer, which require adaptation, and which do not.

## Publication plan
Three focused articles rather than one monolithic document:

| Article | Hypotheses | Focus |
| --- | --- | --- |
| 1 | H1 | Temporal context versus stateless detection at a fixed false-alarm budget |
| 2 | H2, H3 | Uncertainty-aware and safety-constrained defensive decisions |
| 3 | H4 | Transfer of the framework to spacecraft systems |

## Research method
Problem → Literature → Research question → Hypothesis → Mathematical model → Simulation → Baselines → Experiment → Evaluation → Evidence → Publication or prototype.

Research claims must be supported by reproducible, preregistered experiments and a documented comparison to relevant prior work. This repository does not claim operational validation or novelty before evidence is available.

## Project management
- [Master research framework](docs/MASTER_FRAMEWORK.md)
- [Project charter](PROJECT_CHARTER.md)
- [Roadmap](ROADMAP.md)
- [Research log](RESEARCH_LOG.md)
- [Experiment registry](EXPERIMENT_REGISTRY.md)
- [Evidence register](EVIDENCE_REGISTER.md)

## Safety and data
Only authorized, isolated simulations and legally usable data are in scope. Never commit credentials, sensitive operational configurations, confidential financial records, or restricted spacecraft information. Do not target operational satellites, ground stations, or payment systems. The framework is advisory-only.

## Status
**Phase 0 — governance and alignment.** CORE-001 is documented, CORE-002 is implemented and locally unit-tested (11/11), and CORE-003 is specified but not implemented. No experimental results have been reported yet.

## Language
This repository is maintained in English only.

## Reproducibility
Each experiment will record its ID, protocol, environment, code commit, dataset provenance, parameters and seeds (where applicable), baselines, metrics, results, and limitations.

## License and citation
Licensing and citation metadata will be added after review. Public visibility does not automatically grant reuse rights.
