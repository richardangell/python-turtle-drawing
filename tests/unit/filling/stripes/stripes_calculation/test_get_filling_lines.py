from turtle import Vec2D

import pytest

from python_turtle_art.filling.stripes.stripes_calculation import get_filling_lines
from python_turtle_art.lines.line import Line
from python_turtle_art.polygons.kites.convex_kite import ConvexKite


@pytest.fixture(scope="module")
def kite() -> ConvexKite:
    """Kite defined by [(0, 0), (-50, 50), (0, 100), (50, 50)] vertices."""
    return ConvexKite.from_origin_and_dimensions(
        origin=Vec2D(0, 0),
        height=100,
        width=100,
        diagonal_intersection_along_height=0.5,
    )


@pytest.fixture(scope="module")
def square() -> ConvexKite:
    """Square defined by [(-20, -20), (20, -20), (20, 20), (-20, 20)] verrtices."""
    return ConvexKite(
        vertices=(Vec2D(-20, -20), Vec2D(20, -20), Vec2D(20, 20), Vec2D(-20, 20))
    )


def test_horizontal_lines_in_kite(kite):
    expected = [
        Line(vertices=(Vec2D(-10, 10), Vec2D(10, 10))),
        Line(vertices=(Vec2D(-20, 20), Vec2D(20, 20))),
        Line(vertices=(Vec2D(-30, 30), Vec2D(30, 30))),
        Line(vertices=(Vec2D(-40, 40), Vec2D(40, 40))),
        Line(vertices=(Vec2D(-50, 50), Vec2D(50, 50))),
        Line(vertices=(Vec2D(-40, 60), Vec2D(40, 60))),
        Line(vertices=(Vec2D(-30, 70), Vec2D(30, 70))),
        Line(vertices=(Vec2D(-20, 80), Vec2D(20, 80))),
        Line(vertices=(Vec2D(-10, 90), Vec2D(10, 90))),
    ]

    actual = get_filling_lines(gap=10, origin=0, polygon=kite, axis=1)

    assert actual == expected


@pytest.mark.parametrize(
    ["fill_origin", "expected_y_coords"],
    [
        (0, [-18, -15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18]),
        (2, [-19, -16, -13, -10, -7, -4, -1, 2, 5, 8, 11, 14, 17]),
    ],
)
def test_horizontal_lines_in_square(fill_origin, expected_y_coords, square):
    expected = [
        Line(vertices=(Vec2D(20, y_coord), Vec2D(-20, y_coord)))
        for y_coord in expected_y_coords
    ]

    actual = get_filling_lines(gap=3, origin=fill_origin, polygon=square, axis=1)

    assert actual == expected


def test_vertical_lines_in_kite(kite):
    expected = [
        Line(vertices=(Vec2D(-40, 60), Vec2D(-40, 40))),
        Line(vertices=(Vec2D(-30, 70), Vec2D(-30, 30))),
        Line(vertices=(Vec2D(-20, 80), Vec2D(-20, 20))),
        Line(vertices=(Vec2D(-10, 90), Vec2D(-10, 10))),
        Line(vertices=(Vec2D(0, 100), Vec2D(0, 0))),
        Line(vertices=(Vec2D(10, 90), Vec2D(10, 10))),
        Line(vertices=(Vec2D(20, 80), Vec2D(20, 20))),
        Line(vertices=(Vec2D(30, 70), Vec2D(30, 30))),
        Line(vertices=(Vec2D(40, 60), Vec2D(40, 40))),
    ]

    actual = get_filling_lines(gap=10, origin=0, polygon=kite, axis=0)

    assert actual == expected


@pytest.mark.parametrize(
    ["fill_origin", "expected_x_coords"],
    [
        (0, [-18, -15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18]),
        (1, [-17, -14, -11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19]),
    ],
)
def test_vertical_lines_in_square(fill_origin, expected_x_coords, square):
    expected = [
        Line(vertices=(Vec2D(x_coord, -20), Vec2D(x_coord, 20)))
        for x_coord in expected_x_coords
    ]

    actual = get_filling_lines(gap=3, origin=fill_origin, polygon=square, axis=0)

    assert actual == expected
