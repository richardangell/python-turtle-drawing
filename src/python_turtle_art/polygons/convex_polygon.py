from __future__ import annotations

from abc import ABC, abstractmethod
from turtle import RawTurtle, Vec2D

from ..vertices.vertices import DrawMixin, EqMixin, GetExtremeVerticesMixin, RotateMixin
from .is_convex import is_convex


class BaseConvexFill(ABC):
    """Base class for fillers that operate on convex polygons only."""

    @abstractmethod
    def fill(self, turtle: RawTurtle, polygon: ConvexPolygon):
        """Fill."""
        raise NotImplementedError


class ConvexPolygon(DrawMixin, RotateMixin, GetExtremeVerticesMixin, EqMixin):
    """Convex polygon.

    Defines a setter for the vertices property which enforces the convex property.

    """

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Perform checks on vertices and set attributes.

        Check at least 3 vertices are passed and the vertices form a convex polygon are
        provided.

        """
        if len(vertices) < 3:
            raise ValueError("vertices must contain at least 3 points.")
        if not is_convex(vertices):
            raise ValueError("Polygon defined by supplied vertices are not convex.")
        self._vertices = vertices

    def fill(self, turtle: RawTurtle, filler: BaseConvexFill):
        """Fill the polygon."""

        filler.fill(turtle=turtle, polygon=self)

    def is_convex(self) -> bool:
        """Check if the polygon is convex."""
        return is_convex(self.vertices)
