from turtle import Vec2D

import pytest

from python_turtle_art.lines.line import Line
from python_turtle_art.lines.offset_from_line import (
    point_perpendicular_distance_from_line,
)


@pytest.mark.parametrize(
    ["p0", "p1", "distance", "expected"],
    [
        ((0, 0), (0, 10), 10, (-10, 10)),
        ((0, 10), (-10, 10), 10, (-10, 0)),
        ((-10, 10), (-10, 0), 10, (0, 0)),
        ((-10, 0), (0, 0), 10, (0, 10)),
        ((0, 10), (0, 0), 10, (10, 0)),
        ((0, 0), (10, 0), 10, (10, 10)),
        ((10, 0), (10, 10), 10, (0, 10)),
        ((10, 10), (0, 10), 10, (0, 0)),
    ],
)
def test_expected_value_on_right_angled_triangle(p0, p1, distance, expected):
    assert (
        point_perpendicular_distance_from_line(
            p0=Vec2D(*p0), p1=Vec2D(*p1), distance=distance
        )
        == expected
    )


@pytest.mark.parametrize("about_point", [(0, 0), (2, 3), (-1, 2), (3, -4)])
@pytest.mark.parametrize("angle", [30, 47, 112, 180, 340])
@pytest.mark.parametrize(
    ["p0", "p1", "p2", "distance"],
    [
        ((0, 0), (0, 10), (-10, 10), 10),
        ((0, -2), (2, -2), (2, 5), 7),
    ],
)
def test_expected_value_on_rotated_right_angled_triangle(
    p0, p1, p2, distance, angle, about_point
):
    """Test rotated right angled triangle still perpendicular.

    Here a right angled triangle is rotated and we test that the perpendicular point
    from rotated(p0) -> rotated(p1) is rotated(p2).

    """

    line = Line(vertices=(Vec2D(*p0), Vec2D(*p1), Vec2D(*p2)))

    line_rotated = line.rotate(angle=angle, about_point=Vec2D(*about_point))

    expected_perpendicular_point = line_rotated.vertices[2]

    assert point_perpendicular_distance_from_line(
        p0=line_rotated.vertices[0], p1=line_rotated.vertices[1], distance=distance
    ) == pytest.approx(expected_perpendicular_point)
