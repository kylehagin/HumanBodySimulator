"""Stomach organ simulation."""

from ..organ import Organ

class Stomach(Organ):
    """Simulates the stomach for digestion."""

    def __init__(self):
        super().__init__("stomach")
        self.state["pH"] = 2.0
        self.state["contents"] = 0.0  # grams of food

    def update(self, dt: float) -> None:
        """Update digestion processes."""
        if self.state["contents"] > 0:
            digested = min(self.state["contents"], 10.0 * dt)
            self.state["contents"] -= digested
        # pH drifts back toward 2.0
        self.state["pH"] += (2.0 - self.state["pH"]) * 0.5 * dt

    def interact(self, other: Organ) -> None:
        """Interactions with other organs."""
        del other

