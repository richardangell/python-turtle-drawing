"""Base class for fillers that operate on convex polygons."""

from abc import ABC, abstractmethod
from turtle import Turtle, Vec2D


class BaseConvexFill(ABC):
    @abstractmethod
    def fill(self, turtle: Turtle, vertices: tuple[Vec2D, ...]):
        """Fill."""
        raise NotImplementedError
