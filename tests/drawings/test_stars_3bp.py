from pathlib import Path

import pytest
from PIL import Image

from python_turtle_art.drawings import draw_image_stars_3bp
from python_turtle_art.helpers.turtle import turn_off_turtle_animation
from python_turtle_art.write import get_canvas_image

from ..helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((int(1440 * 0.5), int(900 * 0.75)))
def test_image_produced(setup_screen):
    """Check stars_3bp.main.draw_image produces the expected image."""

    # Arrange

    expected_image_file = Path("tests/drawings/expected_images/stars_3bp.png")
    expected_image = Image.open(expected_image_file)

    turtle_, screen = setup_screen
    height, width = screen.screensize()

    # Act

    turn_off_turtle_animation(screen)
    draw_image_stars_3bp(turtle_)

    # Assert

    actual_image = get_canvas_image(screen, height, width)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
