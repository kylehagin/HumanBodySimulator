"""Run a simple body simulation."""

from pathlib import Path
import sys

# Allow running without installing the package
sys.path.append(str(Path(__file__).resolve().parents[1]))

from body_sim.simulation import Simulation

if __name__ == "__main__":
    sim = Simulation()
    sim.run(duration=10.0, dt=1.0)
    print(f"Simulation finished at t={sim.time}")
