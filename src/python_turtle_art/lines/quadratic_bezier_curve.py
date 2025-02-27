from __future__ import annotations

from turtle import Vec2D

import numpy as np

from .line import Line
from .offset_from_line import OffsetFromLine


def quadratic_bezier_curve(t: float, p0: Vec2D, p1: Vec2D, p2: Vec2D):
    """https://en.wikipedia.org/wiki/B%C3%A9zier_curve#Quadratic_B%C3%A9zier_curves"""

    return p1 + (1 - t) ** 2 * (p0 - p1) + t**2 * (p2 - p1)


def get_points_on_quadratic_bezier_curve(
    start: Vec2D,
    end: Vec2D,
    off_line_point: Vec2D,
    steps: int = 10,
) -> tuple[Vec2D, ...]:
    """Get points on quadratic bezier curve.

    Args:
        start (Vec2D): start point of line.
        end (Vec2D): end point of line.
        off_line_point (Vec2D) point off of line to control line curvature.
        steps (int): number of steps to take in line.

    """
    increments = np.linspace(0, 1, steps)

    return tuple(
        quadratic_bezier_curve(increment, start, off_line_point, end)
        for increment in increments
    )


class QuadraticBezierCurve(Line):
    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices

    @classmethod
    def from_start_and_end(
        cls,
        start: Vec2D,
        end: Vec2D,
        off_line: OffsetFromLine | None = None,
        steps: int = 10,
    ) -> QuadraticBezierCurve:
        if start == end:
            raise ValueError("Can only create curve between two different points.")

        if off_line is not None:
            off_line_point = off_line.to_point(start, end)
        else:
            diff = end - start
            off_line_point = Vec2D(start[0] + diff[0] / 2, start[1] + diff[1] / 2)

        vertices = get_points_on_quadratic_bezier_curve(
            start, end, off_line_point, steps
        )

        return QuadraticBezierCurve(vertices=vertices)
