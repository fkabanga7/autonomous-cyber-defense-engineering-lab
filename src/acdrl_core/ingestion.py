"""Strict input validation. Untrusted fields do not authenticate a source."""
from collections.abc import Mapping
from .models import Observation

REQUIRED_STRINGS = (
    "schema_version", "domain_id", "run_id", "event_id",
    "source", "event_type", "asset_id",
)


class InvalidObservation(ValueError):
    """An input violates the observation contract."""


def ingest(record: Mapping) -> Observation:
    if not isinstance(record, Mapping):
        raise InvalidObservation("Observation must be a mapping")
    for key in REQUIRED_STRINGS:
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise InvalidObservation(f"Invalid or missing field: {key}")
    if record["schema_version"] != "0.1":
        raise InvalidObservation("Unsupported schema_version")
    step = record.get("step")
    if type(step) is not int or step < 0:
        raise InvalidObservation("step must be a nonnegative integer")
    attributes = record.get("attributes", {})
    if not isinstance(attributes, dict):
        raise InvalidObservation("attributes must be an object")
    return Observation(
        **{key: record[key] for key in REQUIRED_STRINGS},
        step=step,
        attributes=dict(attributes),
    )
