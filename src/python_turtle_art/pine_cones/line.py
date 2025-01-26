from dataclasses import dataclass
from math import sqrt
from turtle import Turtle, Vec2D
from typing import Optional

import numpy as np


@dataclass
class OffsetFromLine:
    """Class to create a point that is offset from a line.

    Attributes:
        proportion_lenth (float): proportion of the length along the line
            the new point should be placed.
        offset (int): perpendicular distance from line point should be
            placed.

    """

    proportion_lenth: float = 0.5
    offset: int = 10

    def to_point(self, p0: Vec2D, p1: Vec2D) -> Vec2D:
        """Get point that is offset distance from p1 in direction that is
        perpendicular to line p0 -> p1."""

        delta = p1 - p0

        point_along_line = p0 + self.proportion_lenth * delta

        return point_perpendicular_distance_from_line(
            p0=p0, p1=point_along_line, n=self.offset
        )


def point_perpendicular_distance_from_line(p0: Vec2D, p1: Vec2D, n: int) -> Vec2D:
    """Find point which is perpendicular distance n from p1 in line p0, p1."""

    dx, dy = p0 - p1
    dist = sqrt(dx * dx + dy * dy)
    dx /= dist
    dy /= dist

    x3 = p1[0] + n * dy
    y3 = p1[1] - n * dx

    return Vec2D(x3, y3)


def quadratic_bezier_curve(t: float, p0: Vec2D, p1: Vec2D, p2: Vec2D):
    """https://en.wikipedia.org/wiki/B%C3%A9zier_curve#Quadratic_B%C3%A9zier_curves"""

    return p1 + (1 - t) ** 2 * (p0 - p1) + t**2 * (p2 - p1)


def get_points_on_curve(
    start: Vec2D,
    end: Vec2D,
    off_line_point: Vec2D,
    steps: int = 10,
) -> list[Vec2D]:
    """Get points on quadratic bezier curve.

    Args:
        start (Vec2D): start point of line.
        end (Vec2D): end point of line.
        off_line_point (Vec2D) point off of line to control line curvature.
        steps (int): number of steps to take in line.

    """
    increments = np.linspace(0, 1, steps)

    return [
        quadratic_bezier_curve(increment, start, off_line_point, end)
        for increment in increments
    ]


def draw_curved_line(
    turtle: Turtle,
    start: Vec2D,
    end: Vec2D,
    off_line: OffsetFromLine = OffsetFromLine(),
    steps: int = 10,
    draw_points: bool = False,
    size: Optional[int] = None,
) -> None:
    """Draw a curved line.

    Args:
        start (Vec2D): start point of line.
        end (Vec2D): end point of line.
        off_line (OffsetFromLine) definition of point off of line that controls
            line curvature.
        steps (int): number of steps to take in line.
        draw_points (bool): draw the start, end and off_line points that define
            the line.
        size (int): optional width of the line. If not provided the current
            line width is used.

    """
    off_line_point = off_line.to_point(start, end)

    original_pensize = turtle.pensize()
    turtle.pensize(size)

    if draw_points:
        turtle.penup()

        for position in [end, off_line_point, start]:
            turtle.goto(position)
            turtle.dot()

        turtle.pendown()

    for position in get_points_on_curve(start, end, off_line_point, steps):
        turtle.setheading(turtle.towards(position))
        turtle.goto(position)

    turtle.pensize(original_pensize)
