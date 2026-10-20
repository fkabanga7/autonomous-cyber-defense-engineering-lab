"""Validated, minimal domain-independent data contracts."""
from dataclasses import dataclass, field
from typing import Any

ALLOWED_ACTIONS = frozenset({"NO_ACTION", "ALERT_OPERATOR", "REQUEST_HUMAN_REVIEW"})


@dataclass(frozen=True)
class Observation:
    schema_version: str
    domain_id: str
    run_id: str
    event_id: str
    step: int
    source: str
    event_type: str
    asset_id: str
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Finding:
    finding_id: str
    observation_ref: str
    signal: str
    score: float  # Uncalibrated priority, NOT a probability.


@dataclass(frozen=True)
class RiskAssessment:
    finding_id: str
    priority: str
    rationale: str


@dataclass(frozen=True)
class CandidateDecision:
    action: str
    rationale: str


@dataclass(frozen=True)
class SafetyVerdict:
    action: str
    allowed: bool
    executed: bool
    reason: str
