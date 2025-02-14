from dataclasses import dataclass
from math import sqrt
from turtle import Vec2D


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
    offset: int | float = 10

    def to_point(self, p0: Vec2D, p1: Vec2D) -> Vec2D:
        """Get point that is offset distance from p1 in direction that is
        perpendicular to line p0 -> p1."""

        delta = p1 - p0

        point_along_line = p0 + self.proportion_lenth * delta

        return point_perpendicular_distance_from_line(
            p0=p0, p1=point_along_line, n=self.offset
        )


def point_perpendicular_distance_from_line(
    p0: Vec2D, p1: Vec2D, n: int | float
) -> Vec2D:
    """Find point which is perpendicular distance n from p1 in line p0, p1."""

    dx, dy = p0 - p1
    dist = sqrt(dx * dx + dy * dy)
    dx /= dist
    dy /= dist

    x3 = p1[0] + n * dy
    y3 = p1[1] - n * dx

    return Vec2D(x3, y3)
