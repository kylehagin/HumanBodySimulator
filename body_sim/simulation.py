"""Simulation driver for the body."""

from .body import Body

class Simulation:
    """Run the human body simulation."""

    def __init__(self):
        self.body = Body()
        self.time = 0.0

    def step(self, dt: float) -> None:
        """Advance the simulation by dt seconds."""
        self.body.update(dt)
        self.time += dt

    def run(self, duration: float, dt: float = 1.0) -> None:
        """Run the simulation for the given duration."""
        steps = int(duration / dt)
        for _ in range(steps):
            self.step(dt)
