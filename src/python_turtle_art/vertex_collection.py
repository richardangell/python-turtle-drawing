from turtle import Turtle, Vec2D
from typing import Optional, Self, Union

from .fill import BaseFill
from .helpers.rotation import rotate_about_point
from .helpers.turtle import jump_to


class VertexCollection:
    """Base class for a collection of vertices.

    Implements draw and rotate methods.

    Args:
        vertices (tuple[Vec2D, ...]): Vertices in the collection.

    """

    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices

    """The index of the vertex to jump to before drawing lines between points."""
    _jump_to_vertex_index: int

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Set vertices attribute."""
        self._vertices = vertices

    def draw(
        self,
        turtle: Turtle,
        colour: str = "black",
        size: Optional[int] = None,
        fill: Optional[BaseFill] = None,
    ):
        """Set pensize and colour then draw polygon edges."""

        if fill is not None:
            fill.pre_draw(turtle)

        original_colour = turtle.pencolor()
        original_pensize = turtle.pensize()

        turtle.color(colour)
        turtle.pensize(size)

        jump_to(turtle=turtle, position=self.vertices[self._jump_to_vertex_index])

        for point in self.vertices:
            turtle.goto(point)

        turtle.color(original_colour)
        turtle.pensize(original_pensize)

        if fill is not None:
            fill.post_draw(turtle)

    def rotate(self, angle: Union[int, float], about_point: Vec2D) -> Self:
        """Rotate polygon.

        Args:
            angle (Union[int, float]): angle to rotate the polygon.
            about_point (Vec2D): point to rotate about.

        """
        if (angle % 360) != 0:
            self.vertices = tuple(
                rotate_about_point(point, angle, about_point) for point in self.vertices
            )

        return self
