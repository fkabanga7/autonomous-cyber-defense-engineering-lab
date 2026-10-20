"""Canonical records for repeatable, non-sensitive engineering tests."""
import json
from dataclasses import asdict
from .models import Observation, Finding, RiskAssessment, CandidateDecision, SafetyVerdict


def audit_record(
    observation: Observation,
    finding: Finding | None,
    risk: RiskAssessment | None,
    decision: CandidateDecision,
    verdict: SafetyVerdict,
) -> str:
    record = {
        "schema_version": "0.1",
        "run_id": observation.run_id,
        "event_id": observation.event_id,
        "domain_id": observation.domain_id,
        "finding": asdict(finding) if finding else None,
        "risk": asdict(risk) if risk else None,
        "decision": asdict(decision),
        "safety": asdict(verdict),
    }
    return json.dumps(record, sort_keys=True, separators=(",", ":"), allow_nan=False)
