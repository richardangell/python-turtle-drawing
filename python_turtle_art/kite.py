from turtle import Turtle, Vec2D
from helpers import jump_to
from math import sqrt
from typing import Union


class ConvexKite:
    """Class for drawing a convex kite shape."""

    def __init__(
        self,
        origin: Vec2D,
        height: Union[int, float] = sqrt(20),
        width: Union[int, float] = sqrt(20),
        diagonal_intersection_along_height: float = 0.5,
    ):
        self.origin = origin
        self.height = height
        self.width = width
        self.diagonal_intersection_along_height = diagonal_intersection_along_height

        self.half_width = width / 2
        self.points = self._calculate_points()

    def draw(self, turtle: Turtle, fill: bool = False, colour: str = "black"):
        """Draw the diamond shape.

        Args:
            turtle (Turtle): turtle to draw with.
            fill (bool): whether to fill the shape with colour.
            colour (str): colour to use for the shape.

        """
        jump_to(turtle, self.origin)

        original_colour = turtle.pencolor()
        turtle.color(colour)

        if fill:
            turtle.begin_fill()

        for point in reversed(self.points):
            turtle.goto(point)

        if fill:
            turtle.end_fill()

        turtle.color(original_colour)

    def _calculate_points(self):
        """Calculate the points of the kite."""

        left_point = self.origin + Vec2D(
            -self.half_width, self.diagonal_intersection_along_height * self.height
        )
        right_point = self.origin + Vec2D(
            self.half_width, self.diagonal_intersection_along_height * self.height
        )
        top_point = self.origin + Vec2D(0, self.height)

        return (self.origin, left_point, top_point, right_point)
