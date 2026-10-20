"""Advisory-only candidate selection."""
from .models import CandidateDecision, RiskAssessment


def decide(risk: RiskAssessment | None) -> CandidateDecision:
    if risk is None:
        return CandidateDecision("NO_ACTION", "No baseline finding")
    if risk.priority == "HIGH":
        return CandidateDecision("REQUEST_HUMAN_REVIEW", "High priority finding")
    return CandidateDecision("ALERT_OPERATOR", "Review authorization denial")
