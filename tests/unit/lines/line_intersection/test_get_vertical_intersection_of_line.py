from turtle import Vec2D

import pytest

from python_turtle_art.lines.line_intersection import (
    get_vertical_intersection_of_line,
)


def test_vertical_line_exception():
    with pytest.raises(ValueError, match="Line p0, p1 is vertical."):
        get_vertical_intersection_of_line(Vec2D(-1, -1), Vec2D(-1, 1), 5)


@pytest.mark.parametrize(
    ["p0", "p1", "vertical_x", "expected"],
    [
        ((0, 0), (10, 10), 0, (0, 0)),
        ((0, 0), (10, 10), 5, (5, 5)),
        ((0, 0), (10, 10), 10, (10, 10)),
        ((0, 0), (10, 10), 20, (20, 20)),
        ((0, 0), (10, 10), -5, (-5, -5)),
        ((0, 0), (10, 10), -10, (-10, -10)),
        ((-1, -1), (1, -1), 5, (5, -1)),
        ((2, 3), (0, 0), 1, (1, 1.5)),
        ((2, 3), (0, 0), 0, (0, 0)),
        ((2, 3), (0, 0), -1, (-1, -3 / 2)),
        ((2, 3), (0, 0), -2, (-2, -6 / 2)),
        ((2, 3), (0, 0), -3, (-3, -9 / 2)),
        ((2, 3), (0, 0), -4, (-4, -12 / 2)),
    ],
)
def test_expected_output(p0, p1, vertical_x, expected):
    assert get_vertical_intersection_of_line(
        Vec2D(*p0), Vec2D(*p1), vertical_x
    ) == pytest.approx(Vec2D(*expected))
