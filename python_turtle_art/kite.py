from turtle import Turtle, Vec2D
from helpers import jump_to, rotate_about_point
from math import sqrt
from typing import Union

from shape import Shape
from line import get_points_on_curve, OffsetFromLine


class ConvexKite(Shape):
    """Class for drawing a convex kite shape.

    Args:
        origin (Vec2D):
        height (Union[int, float]): height of the kite.
        width (Union[int, float]): width of the kite.
        rotation (Union[int, float]): angle to rotate the kite about origin.
        diagonal_intersection_along_height (float): proportion of the distance
            along the vertical bisector, the vertical bisector intersects with
            the horizontal bisector.

    """

    def __init__(
        self,
        origin: Vec2D,
        height: Union[int, float] = sqrt(20),
        width: Union[int, float] = sqrt(20),
        rotation: Union[int, float] = 0,
        diagonal_intersection_along_height: float = 0.5,
    ):
        """Initialise the ConvexKite object."""
        self.origin = origin
        self.height = height
        self.width = width
        self.rotation = rotation
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

        self._draw_points(turtle)

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

        non_rotated_points = (self.origin, left_point, top_point, right_point)

        if (self.rotation % 360) != 0:
            return tuple(
                rotate_about_point(point, self.rotation, self.origin)
                for point in non_rotated_points
            )

        else:
            return non_rotated_points


class CurvedConvexKite(ConvexKite):
    """Class for drawing a convex kite with curved edges."""

    def __init__(
        self,
        origin: Vec2D,
        off_lines: tuple[OffsetFromLine, ...] = (
            OffsetFromLine(),
            OffsetFromLine(),
            OffsetFromLine(),
            OffsetFromLine(),
        ),
        height: Union[int, float] = sqrt(20),
        width: Union[int, float] = sqrt(20),
        rotation: Union[int, float] = 0,
        diagonal_intersection_along_height: float = 0.5,
    ):
        """Initialise the ConvexKite object."""
        self.origin = origin
        self.off_lines = off_lines
        self.height = height
        self.width = width
        self.rotation = rotation
        self.diagonal_intersection_along_height = diagonal_intersection_along_height

        self.half_width = width / 2
        self.points = self._calculate_points()

    def _calculate_points(self):
        """Calculate the points of the kite."""

        kite_points = super()._calculate_points()

        curved_edges = []

        for index in range(len(kite_points)):
            end_index = index + 1
            if end_index == 4:
                end_index = 0

            control_point = self.off_lines[index].to_point(
                kite_points[index], kite_points[end_index]
            )

            curve_points = get_points_on_curve(
                start=kite_points[index],
                end=kite_points[end_index],
                off_line_point=control_point,
                steps=20,
            )

            curved_edges.extend(curve_points)

        return tuple(curved_edges)
