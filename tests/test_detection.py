import json
import unittest
from acdrl_core.pipeline import process
from test_ingestion import fixture


class PipelineTests(unittest.TestCase):
    def test_normal_no_action(self):
        result = json.loads(process(fixture(event_type="heartbeat")))
        self.assertEqual(result["decision"]["action"], "NO_ACTION")

    def test_denial_alert(self):
        result = json.loads(process(fixture()))
        self.assertEqual(result["decision"]["action"], "ALERT_OPERATOR")
        self.assertFalse(result["safety"]["executed"])

    def test_two_domains_same_pipeline(self):
        for domain in ("spacecraft", "financial"):
            with self.subTest(domain=domain):
                result = json.loads(process(fixture(domain=domain)))
                self.assertEqual(result["decision"]["action"], "ALERT_OPERATOR")

    def test_deterministic(self):
        self.assertEqual(process(fixture()), process(fixture()))
