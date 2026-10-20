import unittest
from acdrl_core.models import CandidateDecision
from acdrl_core.safety import check


class SafetyTests(unittest.TestCase):
    def test_advisory_allowed_but_not_executed(self):
        verdict = check(CandidateDecision("ALERT_OPERATOR", "fixture"))
        self.assertTrue(verdict.allowed)
        self.assertFalse(verdict.executed)

    def test_disruptive_action_vetoed(self):
        verdict = check(CandidateDecision("BLOCK_TRANSACTION", "fixture"))
        self.assertFalse(verdict.allowed)
        self.assertFalse(verdict.executed)

    def test_missing_policy_fails_closed(self):
        verdict = check(CandidateDecision("ALERT_OPERATOR", "fixture"), policy_available=False)
        self.assertFalse(verdict.allowed)
