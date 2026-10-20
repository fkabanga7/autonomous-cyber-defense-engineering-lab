"""Illustrative baseline rule; no ML or attacker attribution."""
from .models import Finding, Observation


def detect(observation: Observation) -> Finding | None:
    # Rule is intentionally simple and shared across domains.
    if observation.event_type != "authorization_denied":
        return None
    return Finding(
        finding_id=f"finding:{observation.event_id}",
        observation_ref=observation.event_id,
        signal="authorization_denied",
        score=0.7,
    )
