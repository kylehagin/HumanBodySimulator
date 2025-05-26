"""Heart organ simulation."""

from math import sin, pi

from ..organ import Organ

class Heart(Organ):
    """Simulates the heart organ."""

    def __init__(self):
        super().__init__("heart")
        self.state["bpm"] = 60  # beats per minute
        self.state["blood_pressure"] = 120.0  # systolic mmHg
        self.state["oxygenated_blood"] = 1.0
        self._time = 0.0

    def update(self, dt: float) -> None:
        """Update heart state over time."""
        self._time += dt
        rate = self.state["bpm"] / 60.0
        # simple pulsatile pressure model
        pulse = 0.5 * (1.0 + sin(2 * pi * self._time * rate))
        self.state["blood_pressure"] = 80.0 + 40.0 * pulse

    def interact(self, other: Organ) -> None:
        """Define interactions with another organ."""
        if other.name == "lungs":
            saturation = other.state.get("oxygen_saturation")
            if saturation is not None:
                self.state["oxygenated_blood"] = saturation

