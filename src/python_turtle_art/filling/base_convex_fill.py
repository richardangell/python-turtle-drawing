"""Base class for fillers that operate on convex polygons."""

from abc import ABC, abstractmethod
from turtle import Turtle


class BaseConvexFill(ABC):
    @abstractmethod
    def pre_draw(self, turtle: Turtle):
        """Pre edge-drawing step."""
        raise NotImplementedError

    @abstractmethod
    def post_draw(self, turtle: Turtle):
        """Post edge-drawing step."""
        raise NotImplementedError
