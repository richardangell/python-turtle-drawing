from abc import ABC, abstractmethod
from turtle import Turtle
from typing import Optional


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def draw(self, turtle: Turtle, fill: bool, colour: str, size: Optional[int] = None):
        """Draw the shape."""
        raise NotImplementedError

    def _draw_points(self, turtle: Turtle) -> None:
        """Draw line connecting points.

        Starts drawing from whatever the current position is.

        """
        if not hasattr(self, "points"):
            raise AttributeError("points have not been set before trying to draw.")

        for point in self.points:
            turtle.goto(point)
