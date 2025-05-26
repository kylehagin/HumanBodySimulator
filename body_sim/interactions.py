"""Definitions of physical and chemical interactions."""

from dataclasses import dataclass

@dataclass
class Chemical:
    name: str
    concentration: float

@dataclass
class PhysicalInteraction:
    description: str
