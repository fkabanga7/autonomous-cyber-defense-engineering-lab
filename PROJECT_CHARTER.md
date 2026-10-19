# ACDRL Project Charter

**Version:** 0.2 — architecture-first revision (2026-10-19)  
**Status:** Research and engineering design; no validated scientific results yet.

## Mission
Design, implement and evaluate a **reusable, safety-aware autonomous cyber-defense engineering framework** for heterogeneous mission-critical systems. Spacecraft and ground-segment systems are the first validation domain; critical financial infrastructure is the second. The defense framework—not a particular simulator—is the primary engineering product.

## Central research question
To what extent can a modular, safety-constrained autonomous cyber-defense architecture detect threats and select effective countermeasures across heterogeneous mission-critical systems while preserving domain-specific operational constraints?

## Scientific and engineering objectives
1. Define a domain-independent core with explicit interfaces for observations, context, detection, risk, decisions, safety policy, response and evaluation.
2. Implement a minimal deterministic core and test harness before domain-specific complexity.
3. Compare transparent rule/statistical baselines with ML only where justified.
4. Specify constraints, uncertainty, authorization, human oversight and auditable outcomes before autonomous action.
5. Validate with a simulated spacecraft and ground-segment adapter.
6. Evaluate independent transfer to a simulated financial payment-infrastructure adapter; measure necessary adaptation and failures rather than assuming generality.
7. Preserve reproducibility and verifiable evidence for research communication.

## Architecture boundaries
**Reusable core:** event normalization, state/context representation, detection interfaces, risk assessment, decision policy, safety gate, response authorization, audit trail and evaluation.

**Domain adapters:** convert native telemetry, command, transaction or infrastructure events to common contracts; provide domain-specific actions, constraints, risk consequences and ground truth for evaluation.

**Simulation/test environments:** generate controlled operating conditions and labeled faults/threats. They are research instruments, not the primary product.

## Scope and exclusions
Included: software engineering, applied mathematics, probabilistic modeling, Monte Carlo evaluation, detection, optimization, graph methods where justified, MDPs and safe/constrained RL as later research.

Excluded: live-system targeting without authorization; automatic disruptive responses in early prototypes; assumptions that cross-domain transfer works without evidence; claims of operational validation or novelty based solely on simulation.

## Research method and evidence
Problem → Literature → Gap assessment → Research question → Hypothesis → Model → Baselines → Controlled experiment → Evaluation → Evidence → Decision. Preserve seeds, configurations, code revision, data provenance, logs, failure cases and limitations. Differentiate learning, engineering validation and scientific novelty.

## Safety and governance
- The core must default to observation/advisory mode until a domain adapter provides approved action capabilities and a safety gate.
- Every decision must be explainable at the interface level and auditable; safety gates can veto actions.
- Domain-specific constraints are authoritative; common abstractions do not erase operational differences.
- Changes to scope or protocol must be logged in RESEARCH_LOG.md.
- The project owner approves GitHub modifications performed by the assistant.
- Public claims must match achieved evidence. No sensitive financial or spacecraft data may be published.

## Existing research assets
The existing ACDRL-SYS-001/002 spacecraft architecture, threat model, mathematical model, telemetry schema and simulation protocol are **retained unchanged** as provisional specifications for the first validation domain. They do not dictate the architecture of the reusable core.

## Initial milestone
**ACDRL-CORE-001:** document core modules, contracts, trust boundaries, safe decision lifecycle, and cross-domain test strategy. Implement a small event-to-advisory pipeline only after reviewing the specification.

## Outputs
Versioned architecture, tested reusable code, domain adapters, reproducible experiment packages, engineering evidence, and scientific manuscripts where justified.
