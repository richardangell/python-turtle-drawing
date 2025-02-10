import os
from pathlib import Path

import pytest
from PIL import Image, ImageChops

from python_turtle_art.cli import setup_turtle_and_screen
from python_turtle_art.drawings import draw_image_pine_cones
from python_turtle_art.helpers.turtle import turn_off_turtle_animation, update_screen
from python_turtle_art.write import get_canvas_image

from .helpers import assert_image_difference_within_tolerance


@pytest.mark.skipif(
    condition=os.getenv("DISABLE_BEARTYPE") is None,
    reason="DISABLE_BEARTYPE environment variable not set",
)
def test_image_produced():
    """Check pine_cones.main.draw_image produces the expected image.

    Note, the function being tested generates lots of random values so if beartype
    is active (with the default configuration, which uses random sampling) then the
    random numbers generated will not be the same as when before beartype was
    introduced. Beartype can be disabled by setting the DISABLE_BEARTYPE environment
    variable, which will allow this test to pass. This test is skipped is the
    DISABLE_BEARTYPE environment variable is not set.

    """

    # Arrange

    expected_image_file = Path("tests/drawings/pine_cones.png")
    expected_image = Image.open(expected_image_file)

    height, width = 4000, 4000
    turtle_, screen = setup_turtle_and_screen(height, width)
    turtle_.hideturtle()

    # Act

    turn_off_turtle_animation()
    draw_image_pine_cones(turtle_)
    update_screen()

    # Assert

    actual_image = get_canvas_image(screen.getcanvas(), height, width)

    difference = ImageChops.difference(actual_image, expected_image)

    assert_image_difference_within_tolerance(
        difference=difference, tolerance_non_matching_pixels=15
    )
