from turtle import Turtle, Vec2D

import numpy as np

from .offset_from_line import OffsetFromLine


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
    off_line: OffsetFromLine | None = None,
    steps: int = 10,
    draw_points: bool = False,
    size: int | float | None = None,
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
    off_line_ = OffsetFromLine() if off_line is None else off_line

    off_line_point = off_line_.to_point(start, end)

    original_pensize = turtle.pensize()
    turtle.pensize(size)  # type: ignore

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
