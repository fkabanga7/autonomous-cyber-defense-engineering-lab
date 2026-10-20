"""Deterministic end-to-end advisory pipeline."""
from collections.abc import Mapping
from .audit import audit_record
from .decision import decide
from .detection import detect
from .ingestion import ingest
from .risk import assess
from .safety import check


def process(record: Mapping, *, policy_available: bool = True) -> str:
    observation = ingest(record)
    finding = detect(observation)
    risk = assess(finding)
    decision = decide(risk)
    verdict = check(decision, policy_available=policy_available)
    return audit_record(observation, finding, risk, decision, verdict)
