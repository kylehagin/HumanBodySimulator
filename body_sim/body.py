"""Representation of the human body."""

from __future__ import annotations
from typing import Iterable

from .organ import Organ
from .organs import Heart, Lungs, Liver, Kidney, Brain, Stomach

class Body:
    """Collection of organs composing the body."""

    def __init__(self, organs: Iterable[Organ] | None = None):
        if organs is None:
            self.organs: list[Organ] = [
                Heart(),
                Lungs(),
                Liver(),
                Kidney(),
                Brain(),
                Stomach(),
            ]
        else:
            self.organs = list(organs)

    def update(self, dt: float) -> None:
        """Update all organs and handle their interactions."""
        for organ in self.organs:
            organ.update(dt)
        # pairwise interactions (simple example)
        for i, organ_a in enumerate(self.organs):
            for organ_b in self.organs[i + 1 :]:
                organ_a.interact(organ_b)
                organ_b.interact(organ_a)
