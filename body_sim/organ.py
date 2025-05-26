"""Base organ class used for simulations."""

from typing import Any

class Organ:
    """Base class for all organs."""

    def __init__(self, name: str):
        self.name = name
        self.state: dict[str, Any] = {}

    def update(self, dt: float) -> None:
        """Update the internal state of the organ."""
        raise NotImplementedError

    def interact(self, other: "Organ") -> None:
        """Interact with another organ."""
        raise NotImplementedError
