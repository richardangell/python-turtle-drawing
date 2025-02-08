from abc import abstractmethod
from turtle import Turtle, Vec2D
from typing import Optional, Self, Union

from .helpers import jump_to
from .fill import BaseFill
from .helpers import rotate_about_point


class Polygon:
    """Class for drawing an arbitrary polygon."""

    _vertices: tuple[Vec2D, ...]

    @abstractmethod
    def calculate_vertices(self) -> tuple[Vec2D, ...]:
        """Calculate vertices for the polygon."""
        raise NotImplementedError

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        if isinstance(vertices, tuple) and all(isinstance(v, Vec2D) for v in vertices):
            if len(vertices) < 2:
                raise ValueError("vertices must have more than one point.")
            self._vertices = vertices
        else:
            raise TypeError("vertices must be a tuple of Vec2D.")

    def draw(self, turtle: Turtle, colour: str = "black", size: Optional[int] = None):
        """Set pensize and colour then draw polygon edges."""

        original_colour = turtle.pencolor()
        original_pensize = turtle.pensize()

        turtle.color(colour)
        turtle.pensize(size)
        self._draw_edges(turtle)

        turtle.color(original_colour)
        turtle.pensize(original_pensize)

    def _draw_edges(self, turtle: Turtle) -> None:
        """Draw the edges of the polygon."""

        self._check_vertices_set()
        jump_to(turtle=turtle, position=self._vertices[-1])

        for point in self._vertices:
            turtle.goto(point)

    def rotate(self, angle: Union[int, float], about_point: Vec2D) -> Self:
        """Rotate polygon.

        Args:
            angle (Union[int, float]): angle to rotate the polygon.
            about_point (Vec2D): point to rotate about.

        """
        self._check_vertices_set()

        if (angle % 360) != 0:
            self.vertices = tuple(
                rotate_about_point(point, angle, about_point) for point in self.vertices
            )

        return self

    def _check_vertices_set(self):
        if not hasattr(self, "_vertices"):
            raise AttributeError("vertices have not been set before trying to draw.")


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
