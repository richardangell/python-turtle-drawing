from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.filling import HorizontalStipeFill
from python_turtle_art.polygons.kites import ConvexKite
from python_turtle_art.write import get_canvas_image

from ....helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_star(setup_screen_with_squares_background):
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    triangle = ConvexKite(
        vertices=(
            Vec2D(-20, -20),
            Vec2D(40, -20),
            Vec2D(40, 10),
            Vec2D(40, 40),
        )
    )
    triangle.draw(turtle, size=1)

    horizontal_stripes = HorizontalStipeFill(gap=2, origin=1, size=1)

    triangle.fill(turtle, horizontal_stripes)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path(
        "tests/component/filling/stripes/expected_horizontal_stripe_fill.png"
    )
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
