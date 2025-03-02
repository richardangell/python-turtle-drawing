from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.filling import VerticalStripeFill
from python_turtle_art.lines import OffsetFromLine
from python_turtle_art.polygons.kites import ConvexCurvedKite
from python_turtle_art.write import get_canvas_image

from ....helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_star(setup_screen_with_squares_background):
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    convex_curved_kite = ConvexCurvedKite.from_origin_and_dimensions(
        origin=Vec2D(10, -40),
        width=70,
        height=50,
        diagonal_intersection_along_height=0.5,
        off_lines=(
            OffsetFromLine(0.5, 10),
            OffsetFromLine(0.5, 10),
            OffsetFromLine(0.5, 10),
            OffsetFromLine(0.5, 10),
        ),
    )
    convex_curved_kite.draw(turtle, size=1)

    vertical_stripes = VerticalStripeFill(gap=3, origin=1, size=1)

    convex_curved_kite.fill(turtle, vertical_stripes)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path(
        "tests/component/filling/stripes/expected_vertical_stripe_fill.png"
    )
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
