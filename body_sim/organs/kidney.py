"""Kidney organ simulation."""

from ..organ import Organ

class Kidney(Organ):
    """Simulates the kidney for waste filtration."""

    def __init__(self):
        super().__init__("kidney")
        self.state["filtration_rate"] = 1.2  # L/hour
        self.state["waste"] = 0.0
        self.state["water_balance"] = 0.0

    def update(self, dt: float) -> None:
        """Update waste filtration."""
        rate = self.state["filtration_rate"]
        self.state["waste"] = max(0.0, self.state["waste"] - rate * dt)

    def interact(self, other: Organ) -> None:
        """Interactions with other organs."""
        del other

