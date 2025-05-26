"""Run a simple body simulation."""

from pathlib import Path
import sys

# Allow running without installing the package
sys.path.append(str(Path(__file__).resolve().parents[1]))

from body_sim.simulation import Simulation

if __name__ == "__main__":
    sim = Simulation()
    duration = 10.0
    dt = 1.0
    steps = int(duration / dt)
    for _ in range(steps):
        sim.step(dt)
        print(f"t={sim.time:.1f}s | heart pressure: {sim.body.organs[0].state['blood_pressure']:.1f} mmHg")
    print(f"Simulation finished at t={sim.time}")

