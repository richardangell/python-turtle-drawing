from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.polygons.kites import Kite
from python_turtle_art.write import get_canvas_image

from ....helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_kite(setup_screen_with_squares_background):
    """Test non-regular kite with vertices manually defined."""
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    Kite(
        vertices=(Vec2D(-30, -30), Vec2D(-20, 30), Vec2D(40, 40), Vec2D(25, -30))
    ).draw(turtle, size=1)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path("tests/component/polygons/kites/expected_kite.png")
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )


@pytest.mark.window_dimensions((100, 100))
def test_arrowhead(setup_screen_with_squares_background):
    """Test diagonal_intersection_along_height > 1 produces an arrow head shape."""
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    Kite.from_origin_and_dimensions(
        origin=Vec2D(-10, -10),
        width=50,
        height=30,
        diagonal_intersection_along_height=1.4,
    ).draw(turtle, size=2)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path("tests/component/polygons/kites/expected_arrowhead.png")
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
