from turtle import Vec2D
from unittest.mock import call

from python_turtle_art.filling.stripes.hash_fill import HashFill
from python_turtle_art.polygons.kites.convex_kite import ConvexKite


def test_get_filling_lines_called_with_both_axes(mocker, mocked_turtle):
    kite = ConvexKite.from_origin_and_dimensions(
        origin=Vec2D(0, 0),
        height=10,
        width=10,
        diagonal_intersection_along_height=0.5,
    )

    fill = HashFill(gap=6, origin=0)

    mocked = mocker.patch(
        "python_turtle_art.filling.stripes.hash_fill.get_filling_lines",
        return_value=[],
    )

    fill.fill(turtle=mocked_turtle, polygon=kite)

    assert mocked.call_count == 2

    mocked.assert_has_calls(
        calls=[
            call(origin=0, gap=6, polygon=kite, axis=0),
            call(origin=0, gap=6, polygon=kite, axis=1),
        ],
        any_order=False,
    )
