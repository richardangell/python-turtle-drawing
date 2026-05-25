from turtle import Vec2D

from ..lines.line import Line
from .is_convex import is_convex


class Polygon(Line):
    """Class for drawing an arbitrary polygon.

    Args:
        vertices (tuple[Vec2D, ...]): Points of the polygon. At least 3 must be
            supplied.

    """

    _jump_to_vertex_index: int = -1

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
