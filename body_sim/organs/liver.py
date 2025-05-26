"""Liver organ simulation."""

from ..organ import Organ

class Liver(Organ):
    """Simulates the liver for metabolic processes."""

    def __init__(self):
        super().__init__("liver")
        self.state["glycogen"] = 100.0  # grams
        self.state["blood_glucose"] = 90.0  # mg/dL

    def update(self, dt: float) -> None:
        """Update metabolic functions."""
        glucose = self.state["blood_glucose"]
        if glucose < 90.0 and self.state["glycogen"] > 0:
            released = min(5.0 * dt, self.state["glycogen"])
            self.state["blood_glucose"] += released
            self.state["glycogen"] -= released

    def interact(self, other: Organ) -> None:
        """Interactions with other organs."""
        # currently no direct interactions
        del other

