from turtle import Vec2D

from ..vertices.vertices import DrawMixin, RotateMixin


class Line(DrawMixin, RotateMixin):
    """Class for drawing a line between arbitrary number of points."""

    _jump_to_vertex_index: int = 0

    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Set vertices attribute and check there are at least 2 points."""
        if len(vertices) < 2:
            raise ValueError("vertices must contain at least 2 points.")
        self._vertices = vertices
