# HumanBodySimulator

This project provides a modular scaffold for simulating the human body. Each organ is
represented as a separate module with its own update and interaction logic. The project
is structured as a Python package named `body_sim`.

## Structure

- `body_sim/organ.py` – base `Organ` class used by all organs.
- `body_sim/organs/` – implementations for specific organs such as the heart, lungs,
  liver, kidney, brain, and stomach.
- `body_sim/body.py` – aggregates multiple organs into a `Body` object and handles their
  interactions.
- `body_sim/interactions.py` – placeholder definitions for physical and chemical
  interactions.
- `body_sim/simulation.py` – a simple driver that steps the simulation forward.
- `scripts/run_simulation.py` – example script that runs a short simulation.

## Running the Example

```bash
python scripts/run_simulation.py
```

This will instantiate a `Simulation` object with a default `Body` containing several
organs and run it for 10 seconds of simulated time.

Organ update and interaction logic is intentionally left as TODOs so that future
contributors can implement detailed physical and chemical processes.
