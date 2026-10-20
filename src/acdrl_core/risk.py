"""Transparent priority classification; not a calibrated risk model."""
from .models import Finding, RiskAssessment


def assess(finding: Finding | None) -> RiskAssessment | None:
    if finding is None:
        return None
    priority = "HIGH" if finding.score >= 0.8 else "MEDIUM"
    return RiskAssessment(finding.finding_id, priority, "Baseline rule priority; uncalibrated")
