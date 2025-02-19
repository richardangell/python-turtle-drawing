from turtle import Vec2D

from python_turtle_art.filling.stripes.horizontal_stripe_fill import HorizontalStipeFill
from python_turtle_art.polygons.kites.convex_kite import ConvexKite


def test_get_filling_lines_called_with_axis_one(mocker, mocked_turtle):
    kite = ConvexKite.from_origin_and_dimensions(
        origin=Vec2D(0, 0),
        height=10,
        width=10,
        diagonal_intersection_along_height=0.5,
    )

    fill = HorizontalStipeFill(gap=6, origin=0)

    mocked = mocker.patch(
        "python_turtle_art.filling.stripes.horizontal_stripe_fill.get_filling_lines",
        return_value=[],
    )

    fill.fill(turtle=mocked_turtle, polygon=kite)

    mocked.assert_called_once_with(origin=0, gap=6, polygon=kite, axis=1)
