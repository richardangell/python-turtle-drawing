"""Mixins providing functionality for collections of vertices."""

from math import inf
from turtle import Turtle, Vec2D
from typing import Optional, Self, Union

from ..helpers.rotation import rotate_about_point
from ..helpers.turtle import jump_to


class VerticesMixin:
    """Mixin class for a collection of vertices."""

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Set vertices attribute."""
        self._vertices = vertices


class DrawMixin(VerticesMixin):
    """Mixin class for drawing a collection of vertices."""

    """The index of the vertex to jump to before drawing lines between points."""
    _jump_to_vertex_index: int

    def draw(
        self,
        turtle: Turtle,
        colour: str = "black",
        size: Optional[int] = None,
    ):
        """Set pensize and colour then draw polygon edges."""

        original_colour = turtle.pencolor()
        original_pensize = turtle.pensize()

        turtle.pencolor(colour)
        turtle.pensize(size)

        jump_to(turtle=turtle, position=self.vertices[self._jump_to_vertex_index])

        for point in self.vertices:
            turtle.goto(point)

        turtle.pencolor(original_colour)
        turtle.pensize(original_pensize)


class RotateMixin(VerticesMixin):
    """Mixin class for rotating a collection of vertices."""

    def rotate(self, angle: Union[int, float], about_point: Vec2D) -> Self:
        """Rotate vertices.

        Args:
            angle (Union[int, float]): angle, in degrees, to rotate the vertices.
            about_point (Vec2D): point to rotate about.

        """
        if (angle % 360) != 0:
            self.vertices = tuple(
                rotate_about_point(point, angle, about_point) for point in self.vertices
            )

        return self


class GetExtremeVerticesMixin(VerticesMixin):
    """Mixin class for getting extreme vertices."""

    def get_extreme_y_vertices_indices(self) -> tuple[int, int]:
        """Get the indices of the vertices with min and max y values."""

        minimum_y = inf
        maximum_y = -inf

        minimum_y_index = -1
        maximum_y_index = -1

        for vertex_index, vertex in enumerate(self.vertices):
            if vertex[1] < minimum_y:
                minimum_y = vertex[1]
                minimum_y_index = vertex_index

            if vertex[1] > maximum_y:
                maximum_y = vertex[1]
                maximum_y_index = vertex_index

        if minimum_y_index == -1 or maximum_y_index == -1:
            raise ValueError("Failed to find min or max y index.")

        return minimum_y_index, maximum_y_index
