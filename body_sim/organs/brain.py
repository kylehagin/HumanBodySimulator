"""Brain organ simulation."""

from random import uniform

from ..organ import Organ

class Brain(Organ):
    """Simulates the brain for neural activity."""

    def __init__(self):
        super().__init__("brain")
        self.state["neural_activity"] = 0.5

    def update(self, dt: float) -> None:
        """Update neural activity."""
        baseline = 0.5
        current = self.state["neural_activity"]
        # approach baseline with small random variation
        self.state["neural_activity"] = current + (baseline - current) * 0.1 * dt
        self.state["neural_activity"] += uniform(-0.01, 0.01) * dt

    def interact(self, other: Organ) -> None:
        """Interactions with other organs."""
        del other

