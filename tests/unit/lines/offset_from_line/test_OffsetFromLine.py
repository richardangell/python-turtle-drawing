from math import sqrt
from turtle import Vec2D

import pytest

from python_turtle_art.lines.offset_from_line import (
    OffsetFromLine,
    point_perpendicular_distance_from_line,
)


@pytest.mark.parametrize(
    ["proportion_lenth", "offset", "p0", "p1", "expected"],
    [
        (0.5, 10, (0, 0), (10, 0), (5, 10)),
        (0.3, 10, (0, 0), (10, 0), (3, 10)),
        (0.5, sqrt(25 + 25), (0, 0), (10, 10), (0, 10)),
        (0.1, sqrt(101), (0, 0), (100, 10), (9, 11)),
    ],
)
def test_to_point(proportion_lenth, offset, p0, p1, expected):
    """Test OffsetFromLine.to_point outputs the expected value."""

    offset = OffsetFromLine(proportion_lenth=proportion_lenth, offset=offset)

    assert offset.to_point(Vec2D(*p0), Vec2D(*p1)) == expected


@pytest.mark.parametrize(
    ["proportion_lenth", "offset", "p0", "p1"],
    [
        (0.5, 10, (0, 0), (10, 0)),
        (0.3, 3, (-3, 9), (0, 17)),
        (0.2, 6, (-3, -4), (12, 21)),
        (1.3, 3, (-3, 9), (0, 17)),
    ],
)
def test_to_point_by_constructing_rectangle(proportion_lenth, offset, p0, p1):
    offset_from_line = OffsetFromLine(proportion_lenth=proportion_lenth, offset=offset)

    p0_ = Vec2D(*p0)
    p1_ = Vec2D(*p1)
    diff_p1_p0 = p1_ - p0_
    dist_p0_to_p1 = sqrt(diff_p1_p0[0] ** 2 + diff_p1_p0[1] ** 2)

    # 3rd rectangle point
    p2 = point_perpendicular_distance_from_line(p0=p0_, p1=p1_, distance=offset)

    # 4th rectangle point
    p3 = point_perpendicular_distance_from_line(p0=p1_, p1=p2, distance=dist_p0_to_p1)

    diff_p3_p2 = p3 - p2

    # expected point is 1 - proportion_lenth along the line from p2 to p3
    expected = (
        p2[0] + diff_p3_p2[0] * (1 - proportion_lenth),
        p2[1] + diff_p3_p2[1] * (1 - proportion_lenth),
    )

    actual = offset_from_line.to_point(p0_, p1_)

    assert actual == pytest.approx(expected)
