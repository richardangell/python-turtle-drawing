from turtle import Turtle, Vec2D

from ..filling.base_fill import BaseFill
from ..vertices.vertices import DrawMixin, RotateMixin
from .is_convex import is_convex


class Polygon(DrawMixin, RotateMixin):
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

    def draw(
        self,
        turtle: Turtle,
        colour: str = "black",
        size: int | None = None,
        fill: BaseFill | None = None,
    ):
        """Set pensize and colour then draw polygon edges."""

        if fill is not None:
            fill.pre_draw(turtle)

        super().draw(turtle=turtle, colour=colour, size=size)

        if fill is not None:
            fill.post_draw(turtle)

    def is_convex(self) -> bool:
        """Check if the polygon is convex."""
        return is_convex(self.vertices)
