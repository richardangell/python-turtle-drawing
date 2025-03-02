from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.filling import ColourFill
from python_turtle_art.polygons.polygon import Polygon
from python_turtle_art.write import get_canvas_image

from ...helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_colour_fill(setup_screen_with_squares_background):
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    coordinates = [
        [0, 5],
        [1, 10],
        [2, 5],
        [10, 5],
        [3, 2],
        [6, -10],
        [1, 0],
        [-5, -10],
        [-2, 2],
        [-9, 5],
    ]

    star = Polygon(vertices=tuple(3 * Vec2D(*coords) for coords in coordinates))

    star.draw(turtle, size=2)

    star.fill(turtle, ColourFill("blue"))

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path("tests/component/filling/expected_colour_fill.png")
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
