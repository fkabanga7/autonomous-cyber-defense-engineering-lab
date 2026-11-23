# ACDRL — Master Research and Engineering Framework

**Version:** 1.1 (English repository edition) | **Date:** 2026-11-23  
**Status:** Scientific direction and abstract approved. Chapter structure proposed. No chapters of the master document are drafted in this repository. The master document is drafted in French and translated to English for this repository.

## Research identity

| Item | Statement |
| --- | --- |
| Central focus | Autonomous cyber-defense decision-making under uncertainty and operational constraints |
| System type | Integrated detection, AI-supported decision-making, and independent safety enforcement |
| Primary validation domain | Critical financial payment systems |
| Second validation domain | Spacecraft and ground-segment systems |
| Method | Mathematical modeling, reproducible simulation, cybersecurity engineering, and evidence-gated evaluation |
| Engineering maturity | CORE-001 documented; CORE-002 implemented and locally unit-tested (11/11); CORE-003 specified, not implemented |

## Approved abstract
Critical financial systems operate in environments where cyber threats, incomplete information, and strict availability requirements make defensive decision-making particularly challenging. Although cybersecurity monitoring can identify suspicious activities, detecting a potential threat does not necessarily determine the most appropriate response. An excessive defensive intervention may disrupt legitimate operations, while an insufficient response may allow a threat to escalate. The fundamental challenge is therefore to select effective defensive actions under uncertainty while preserving operational safety and continuity.

The Autonomous Cyber Defense Engineering Lab (ACDRL) investigates the design and experimental validation of an integrated cyber-defense framework combining security monitoring, contextual threat detection, uncertainty assessment, intelligent decision-making, and independent safety enforcement. Its primary objective is to develop and evaluate methods for selecting defensive responses that balance cybersecurity effectiveness, operational consequences, and explicitly defined safety constraints.

The framework adopts a modular architecture in which observations are processed through detection, risk assessment, candidate decision generation, safety evaluation, and audit mechanisms. Mathematical modeling provides the foundation for representing system conditions, uncertainty, response costs, and operational constraints. Machine learning and optimization techniques will be introduced progressively where they demonstrate measurable advantages over simpler baseline methods.

The research begins with critical financial payment systems, using synthetic events and isolated simulations to examine threats affecting authentication, transaction processing, service availability, and supporting infrastructure. A subsequent research stage will investigate whether the developed methods can be adapted to spacecraft and ground-segment systems without compromising domain-specific safety requirements.

The engineering methodology follows an evidence-driven progression from deterministic prototypes to temporal detection, uncertainty-aware analysis, constrained decision optimization, and controlled experimental evaluation. Each stage requires reproducible tests, baseline comparisons, documented limitations, and explicit verification of safety properties before advancing.

At the current stage, ACDRL has documented its initial modular architecture and implemented a deterministic, advisory-only Python prototype. Eleven unit tests have passed, providing preliminary evidence of correct behavior for selected ingestion, detection, decision, and safety functions. These results do not yet establish autonomous operational capability or real-world cybersecurity effectiveness.

The expected contribution is an experimentally evaluated approach to cyber-defense decision-making in which uncertainty, operational constraints, and independent safety controls are incorporated into the selection and assessment of defensive responses. The research aims to determine when increasingly autonomous methods offer measurable benefits over conventional advisory approaches, and under which conditions human intervention remains necessary.

**Keywords:** Autonomous Cyber Defense; Critical Financial Systems; Decision-Making Under Uncertainty; Cyber Resilience; Safety-Constrained Optimization; Contextual Threat Detection; Artificial Intelligence; Payment Systems; Spacecraft Cybersecurity.

## Central research problem
How can an autonomous cyber-defense system select effective defensive actions under uncertainty while respecting operational constraints and preserving the resilience of critical systems, evaluated first in financial payment systems?

## Research principles
1. Attack the concrete engineering problem rather than adding unnecessary theory.
2. Use mathematics and AI only where they support a testable mechanism.
3. Treat detection, uncertainty, recommendation, permission, and execution as distinct functions.
4. Validate first in financial systems; evaluate spacecraft transfer separately and last.
5. Maintain independent safety enforcement and human authorization for consequential actions.
6. Make no scientific performance claims before reproducible, preregistered experiments.

## System progression

| Level | Capability | Status |
| --- | --- | --- |
| 1 | Deterministic advisory detection and safety checks (CORE-002) | Implemented, unit-tested |
| 2 | Bounded temporal context and configurable detection (CORE-003) | Specified |
| 3 | Explicit uncertainty, missingness, and abstention (CORE-004) | Planned |
| 4 | Safe multi-objective defensive decision selection (CORE-005) | Planned |
| 5 | Controlled comparative simulation and validation (CORE-006 and domain testbeds) | Planned |

## Publication plan
Article 1 tests H1 (temporal context versus stateless detection). Article 2 tests H2 and H3 (uncertainty-aware and safety-constrained decisions). Article 3 reports the spacecraft transfer evaluation (H4).

## Proposed table of contents (awaiting owner approval)

### General Introduction (domain-neutral)
0.1 Digital transformation and cybersecurity challenges in critical systems · 0.2 Why detection alone is insufficient · 0.3 Defensive decisions under uncertainty · 0.4 Research question and hypotheses · 0.5 Objectives and expected contributions · 0.6 Methodology and evidence requirements · 0.7 Scope, limitations and organization

### Part I — Research Foundations
- **Chapter 1.** Cybersecurity and Operational Resilience of Critical Financial Systems: payment ecosystem architecture; assets, trust boundaries and attack surfaces; threats to transaction processing and availability; interdependencies and cascading failures; defensive actions and unintended consequences; safety and continuity requirements. *Deliverable: threat and operational-constraint model (see ACDRL-FIN-001).*
- **Chapter 2.** Existing Cyber-Defense Approaches and Research Gaps: signature and rule-based detection; behavioral and temporal anomaly detection; orchestration and automated response; AI agents and autonomous cyber defense; safety-aware and uncertainty-aware decision systems; comparative assessment; gaps and positioning. *Deliverable: literature matrix.*
- **Chapter 3.** Mathematical Foundations of Cyber-Defense Decisions: states, observations and actions; temporal dynamics; partial observability; loss and impact functions; hard constraints and feasible action sets; multi-objective and constrained optimization; formal hypotheses. *Deliverable: testable formulation.*

### Part II — System Architecture and Engineering
- **Chapter 4.** Modular Architecture and Engineering Contracts (CORE-001).
- **Chapter 5.** Deterministic Cyber-Defense Baseline (CORE-002).
- **Chapter 6.** Temporal Context and Intelligent Threat Detection (CORE-003).
- **Chapter 7.** Uncertainty-Aware and Safety-Constrained Decision-Making (CORE-004 and CORE-005).

### Part III — Simulation and Experimental Validation
- **Chapter 8.** Financial Payment System Modeling and Simulation (ACDRL-FIN-001 and generator).
- **Chapter 9.** Experimental Design, Baselines, and Evaluation Metrics.
- **Chapter 10.** Experimental Results and Comparative Analysis (written only after experiments).

### Part IV — Cross-Domain Validation and Research Synthesis
- **Chapter 11.** Transfer Evaluation in Spacecraft Systems.
- **Chapter 12.** Research Contributions, Limitations, and Future Engineering.

**Appendices:** references; glossary; mathematical notation; versioned interface contracts; algorithms; scenario configurations; test reports; experiment registry; evidence register; reproducibility instructions.

## Engineering-to-chapter alignment

| Engineering item | Chapter | Status |
| --- | --- | --- |
| CORE-001 | 4 | Documented |
| CORE-002 | 5 | Implemented, unit-tested |
| CORE-003 | 6 | Specified |
| CORE-004 / CORE-005 | 7 | Planned |
| Financial testbed (minimal version built in parallel with CORE-003) | 8 | Planned |
| H1, H2, H3 experiments | 9–10 | Planned |
| Spacecraft validation | 11 | Planned |

## Writing order
Part I and the General Introduction can be written now. Technical chapters are written as the corresponding implementation is completed. Chapter 10 is written only after the experiments have been run.

## Change control
Changes to this document are logged in `RESEARCH_LOG.md`. Scientific claims follow the rules in `EVIDENCE_REGISTER.md`.
