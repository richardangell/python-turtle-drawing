import os
from pathlib import Path

import pytest
from PIL import Image

from python_turtle_art.drawings import draw_image_pine_cones
from python_turtle_art.helpers.turtle import turn_off_turtle_animation, update_screen
from python_turtle_art.write import get_canvas_image

from ..helpers import assert_image_difference_within_tolerance


@pytest.mark.skipif(
    condition=os.getenv("DISABLE_BEARTYPE") is None,
    reason="DISABLE_BEARTYPE environment variable not set",
)
@pytest.mark.screen_dimensions((4000, 4000))
@pytest.mark.window_dimensions((1440 * 0.5, 900 * 0.75))
@pytest.mark.slow
def test_image_produced(setup_screen):
    """Check pine_cones.main.draw_image produces the expected image.

    Note, the function being tested generates lots of random values so if beartype
    is active (with the default configuration, which uses random sampling) then the
    random numbers generated will not be the same as when before beartype was
    introduced. Beartype can be disabled by setting the DISABLE_BEARTYPE environment
    variable, which will allow this test to pass. This test is skipped is the
    DISABLE_BEARTYPE environment variable is not set.

    """

    # Arrange

    expected_image_file = Path("tests/drawings/expected_images/pine_cones.png")
    expected_image = Image.open(expected_image_file)

    turtle_, screen = setup_screen
    height, width = screen.screensize()

    # Act

    turn_off_turtle_animation(screen)
    draw_image_pine_cones(turtle_)
    update_screen(screen)

    # Assert

    actual_image = get_canvas_image(screen, height, width)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=23,
        tolerance_adjacent_pixels=1,
    )
