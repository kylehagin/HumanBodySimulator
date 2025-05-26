"""Lungs organ simulation."""

from math import exp

from ..organ import Organ

class Lungs(Organ):
    """Simulates the lungs for gas exchange."""

    def __init__(self):
        super().__init__("lungs")
        self.state["oxygen_saturation"] = 0.98

    def update(self, dt: float) -> None:
        """Update lung oxygen exchange."""
        target = 0.98
        current = self.state["oxygen_saturation"]
        # exponential decay toward target
        self.state["oxygen_saturation"] = target - (target - current) * exp(-dt)

    def interact(self, other: Organ) -> None:
        """Interactions with other organs, e.g. heart."""
        # Lungs primarily provide oxygen information to the heart; no action here.
        del other

