from turtle import Vec2D

import pytest

from python_turtle_art.lines.line_intersection import (
    get_horizontal_intersection_of_line,
)


def test_vertical_line_exception():
    with pytest.raises(ValueError, match="Line p0, p1 is horizontal."):
        get_horizontal_intersection_of_line(Vec2D(-1, -1), Vec2D(1, -1), 5)


@pytest.mark.parametrize(
    ["p0", "p1", "horizontal_y", "expected"],
    [
        ((0, 0), (10, 10), 0, (0, 0)),
        ((0, 0), (10, 10), 5, (5, 5)),
        ((0, 0), (10, 10), 10, (10, 10)),
        ((0, 0), (10, 10), 20, (20, 20)),
        ((0, 0), (10, 10), -5, (-5, -5)),
        ((0, 0), (10, 10), -10, (-10, -10)),
        ((-1, -1), (-1, 1), 5, (-1, 5)),
        ((2, 3), (0, 0), 1.5, (1, 1.5)),
        ((2, 3), (0, 0), 0, (0, 0)),
        ((2, 3), (0, 0), -1, (-2 / 3, -1)),
        ((2, 3), (0, 0), -2, (-4 / 3, -2)),
        ((2, 3), (0, 0), -3, (-2, -3)),
        ((2, 3), (0, 0), -4, (-8 / 3, -4)),
    ],
)
def test_expected_output(p0, p1, horizontal_y, expected):
    assert get_horizontal_intersection_of_line(
        Vec2D(*p0), Vec2D(*p1), horizontal_y
    ) == pytest.approx(Vec2D(*expected))
