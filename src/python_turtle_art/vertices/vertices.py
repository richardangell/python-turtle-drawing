"""Mixins providing functionality for collections of vertices."""

from collections import namedtuple
from enum import Enum
from math import inf
from turtle import Turtle, Vec2D
from typing import Any, Optional, Self, Union

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


ExtremeIndices = namedtuple("ExtremeIndices", ["minimum", "maximum"])


class Axis(Enum):
    """Enum for x and y axes."""

    x = 0
    y = 1


class GetExtremeVerticesMixin(VerticesMixin):
    """Mixin class for getting extreme vertices."""

    def get_vertices_indices_with_min_and_max_values_on_axis(
        self, axis=0
    ) -> ExtremeIndices:
        """Get the indices of the vertices with min and max x or y values.

        Args:
            axis (int): 0 for x axis, 1 for y axis.

        """
        axis_enum = Axis(axis)

        minimum = inf
        maximum = -inf

        minimum_index = -1
        maximum_index = -1

        for vertex_index, vertex in enumerate(self.vertices):
            if vertex[axis] < minimum:
                minimum = vertex[axis]
                minimum_index = vertex_index

            if vertex[axis] > maximum:
                maximum = vertex[axis]
                maximum_index = vertex_index

        if minimum_index == -1 or maximum_index == -1:
            raise ValueError(f"Failed to find min or max {axis_enum.name} index.")

        return ExtremeIndices(minimum=minimum_index, maximum=maximum_index)


class EqMixin(VerticesMixin):
    """Mixin providing __eq__ method that compares vertices attribute."""

    def __eq__(self, other: Any) -> bool:
        """Check if vertices are equal."""
        if not isinstance(other, EqMixin):
            return False
        else:
            return self.vertices == other.vertices
