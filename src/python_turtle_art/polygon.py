from abc import abstractmethod
from turtle import Turtle, Vec2D
from typing import Optional, Self, Union

from .fill import BaseFill
from .helpers import jump_to, rotate_about_point


class Polygon:
    """Class for drawing an arbitrary polygon.

    Args:
        vertices (tuple[Vec2D, ...]): Points of the polygon.

    """

    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices

    @abstractmethod
    def calculate_vertices(self) -> tuple[Vec2D, ...]:
        """Calculate vertices for the polygon."""
        raise NotImplementedError

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        if len(vertices) < 3:
            raise ValueError("vertices must contain at least 3 points.")
        self._vertices = vertices

    def draw(self, turtle: Turtle, colour: str = "black", size: Optional[int] = None):
        """Set pensize and colour then draw polygon edges."""

        original_colour = turtle.pencolor()
        original_pensize = turtle.pensize()

        turtle.color(colour)
        turtle.pensize(size)

        jump_to(turtle=turtle, position=self._vertices[-1])

        for point in self._vertices:
            turtle.goto(point)

        turtle.color(original_colour)
        turtle.pensize(original_pensize)

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


class ConvexPolygon(Polygon):
    """Class for drawing a convex polygon."""

    def draw(
        self,
        turtle: Turtle,
        colour: str = "black",
        size: Optional[int] = None,
        fill: Optional[BaseFill] = None,
    ):
        """Draw polygon with optional filling."""

        if fill is not None:
            fill.pre_draw(turtle)

        super().draw(turtle=turtle, colour=colour, size=size)

        if fill is not None:
            fill.post_draw(turtle)
