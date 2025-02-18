from turtle import Vec2D

import pytest

from python_turtle_art.filling.horizontal_stripe_fill import HorizontalStipeFill
from python_turtle_art.lines.line import Line
from python_turtle_art.polygons.convex_polygon import ConvexPolygon
from python_turtle_art.polygons.kites.convex_kite import ConvexKite


def test_get_filling_lines_in_kite():
    horizontal_stripe_fill = HorizontalStipeFill(gap=10, origin=0)

    kite = ConvexKite.from_origin_and_dimensions(
        origin=Vec2D(0, 0),
        height=100,
        width=100,
        diagonal_intersection_along_height=0.5,
    )

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

    actual = horizontal_stripe_fill.get_filling_lines(polygon=kite)

    assert actual == expected


@pytest.mark.parametrize(
    ["fill_origin", "expected_y_coords"],
    [
        (0, [-18, -15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18]),
        (2, [-19, -16, -13, -10, -7, -4, -1, 2, 5, 8, 11, 14, 17]),
    ],
)
def test_get_filling_lines_in_square(fill_origin, expected_y_coords):
    horizontal_stripe_fill = HorizontalStipeFill(gap=3, origin=fill_origin)

    square = ConvexPolygon(
        vertices=(Vec2D(-20, -20), Vec2D(20, -20), Vec2D(20, 20), Vec2D(-20, 20))
    )

    expected = [
        Line(vertices=(Vec2D(20, y_coord), Vec2D(-20, y_coord)))
        for y_coord in expected_y_coords
    ]

    actual = horizontal_stripe_fill.get_filling_lines(polygon=square)

    assert actual == expected
