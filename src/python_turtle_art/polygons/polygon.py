from __future__ import annotations

from abc import abstractmethod
from turtle import RawTurtle, Vec2D

from ..vertices.vertices import DrawMixin, EqMixin, GetExtremeVerticesMixin, RotateMixin
from .convex_polygon import BaseConvexFill, ConvexPolygon
from .is_convex import is_convex


class BaseFill(BaseConvexFill):
    """Base class for fillers.

    Subclasses of BaseFill can operate on convex and non-convex polygons.

    """

    @abstractmethod
    def fill(self, turtle: RawTurtle, polygon: Polygon | ConvexPolygon):
        """Fill."""
        raise NotImplementedError


class Polygon(DrawMixin, RotateMixin, GetExtremeVerticesMixin, EqMixin):
    """Class for drawing an arbitrary polygon.

    Args:
        vertices (tuple[Vec2D, ...]): Points of the polygon. At least 3 must be
            supplied.

    """

    _jump_to_vertex_index: int = -1

    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Set vertices attribute and check there are at least 3 points."""
        if len(vertices) < 3:
            raise ValueError("vertices must contain at least 3 points.")
        self._vertices = vertices

    def is_convex(self) -> bool:
        """Check if the polygon is convex."""
        return is_convex(self.vertices)

    def fill(self, turtle: RawTurtle, filler: BaseFill):
        """Fill the polygon."""

        filler.fill(turtle=turtle, polygon=self)
