import unittest
from acdrl_core.ingestion import ingest, InvalidObservation


def fixture(domain="spacecraft", event_type="authorization_denied"):
    return {
        "schema_version": "0.1",
        "domain_id": domain,
        "run_id": "fixture-001",
        "event_id": "evt-001",
        "step": 10,
        "source": "sim-adapter",
        "event_type": event_type,
        "asset_id": "synthetic-asset-1",
        "attributes": {"authorization_result": "denied"},
    }


class IngestionTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(ingest(fixture()).step, 10)

    def test_invalid_schema(self):
        record = fixture()
        record["schema_version"] = "unknown"
        with self.assertRaises(InvalidObservation):
            ingest(record)

    def test_bool_step_rejected(self):
        record = fixture()
        record["step"] = True
        with self.assertRaises(InvalidObservation):
            ingest(record)

    def test_missing_field(self):
        record = fixture()
        del record["event_id"]
        with self.assertRaises(InvalidObservation):
            ingest(record)
