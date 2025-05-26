# Organ Model Overview

This document outlines the simplified models implemented for each organ in the simulation. The intent is to demonstrate how biochemical processes and basic physical dynamics can be approximated in code without relying on external dependencies.

## Heart
- **State Variables**: `bpm`, `blood_pressure`, `oxygenated_blood`.
- **Update**: Heart rate (`bpm`) and blood pressure are updated using a simple sinusoidal model to emulate pulsatile flow. The oxygenation level of the blood is driven by interaction with the lungs.
- **Interactions**: Receives oxygen saturation from the lungs and shares blood pressure data with other organs.

## Lungs
- **State Variables**: `oxygen_saturation`.
- **Update**: Oxygen saturation gradually moves toward atmospheric levels (assumed 98%) using an exponential decay model.
- **Interactions**: Provides the current oxygen saturation to the heart.

## Liver
- **State Variables**: `glycogen`, `blood_glucose`.
- **Update**: Glycogen is converted to glucose when blood glucose drops below a threshold.
- **Interactions**: Supplies glucose to the bloodstream for use by other organs.

## Kidney
- **State Variables**: `waste`, `water_balance`.
- **Update**: Filters waste and adjusts water balance in proportion to the filtration rate.
- **Interactions**: Shares water and waste levels with other organs (not yet fully modeled).

## Brain
- **State Variables**: `neural_activity`.
- **Update**: Activity trends toward a baseline with minor random noise.
- **Interactions**: Can influence the heart rate in later versions of the simulation.

## Stomach
- **State Variables**: `contents`, `pH`.
- **Update**: Contents are broken down over time while the pH slowly returns to its acidic baseline.
- **Interactions**: Sends nutrients to the liver as digestion proceeds.

These models are intentionally simple but aim to capture a small slice of real biochemical and physical behaviors to make the simulation feel more lifelike.
