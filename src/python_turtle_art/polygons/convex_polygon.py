from turtle import Turtle, Vec2D

from ..filling.base_convex_fill import BaseConvexFill
from ..filling.base_fill import BaseFill
from ..vertices.vertices import DrawMixin, RotateMixin
from .is_convex import is_convex


class ConvexPolygon(DrawMixin, RotateMixin):
    """Mixin for a convex polygon.

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

    def fill(self, turtle: Turtle, filler: BaseConvexFill | BaseFill):
        """Fill the polygon."""

        filler.fill(turtle=turtle, vertices=self.vertices)

    def is_convex(self) -> bool:
        """Check if the polygon is convex."""
        return is_convex(self.vertices)
