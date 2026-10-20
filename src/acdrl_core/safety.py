"""Independent fail-closed safety policy for the research MVP."""
from .models import ALLOWED_ACTIONS, CandidateDecision, SafetyVerdict


def check(candidate: CandidateDecision, policy_available: bool = True) -> SafetyVerdict:
    if not policy_available:
        return SafetyVerdict(candidate.action, False, False, "MISSING_POLICY")
    if candidate.action not in ALLOWED_ACTIONS:
        return SafetyVerdict(candidate.action, False, False, "ACTION_NOT_PERMITTED")
    return SafetyVerdict(candidate.action, True, False, "ADVISORY_ONLY")
