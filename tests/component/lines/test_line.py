from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.lines import Line
from python_turtle_art.write import get_canvas_image

from ...helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_diagonal_lines(setup_screen_with_squares_background):
    """Test diagonal lines of different lengths and thickness."""
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    Line(vertices=(Vec2D(-40, -40), Vec2D(40, 40))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-30, -40), Vec2D(40, 30))).draw(turtle, size=2)
    Line(vertices=(Vec2D(-20, -40), Vec2D(40, 20))).draw(turtle, size=3)
    Line(vertices=(Vec2D(-10, -40), Vec2D(40, 10))).draw(turtle, size=4)

    Line(vertices=(Vec2D(-40, 10), Vec2D(-40, 40))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-40, 10), Vec2D(-20, 35))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-40, 10), Vec2D(-10, 10))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-40, 10), Vec2D(-20, -10))).draw(turtle, size=1)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path("tests/component/lines/expected_diagonal_lines.png")
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )


@pytest.mark.window_dimensions((100, 100))
def test_vertical_lines(setup_screen_with_squares_background):
    """Test vertical lines of different lengths and thickness."""
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    Line(vertices=(Vec2D(-40, 10), Vec2D(-40, 40))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-35, -10), Vec2D(-35, 40))).draw(turtle, size=2)
    Line(vertices=(Vec2D(-25, -25), Vec2D(-25, 40))).draw(turtle, size=4)
    Line(vertices=(Vec2D(-10, -40), Vec2D(-10, 40))).draw(turtle, size=6)

    Line(vertices=(Vec2D(10, -40), Vec2D(10, 40))).draw(turtle, size=1)
    Line(vertices=(Vec2D(20, -40), Vec2D(20, 25))).draw(turtle, size=1)
    Line(vertices=(Vec2D(30, -40), Vec2D(30, 10))).draw(turtle, size=1)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path("tests/component/lines/expected_vertical_lines.png")
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )


@pytest.mark.window_dimensions((100, 100))
def test_horizontal_lines(setup_screen_with_squares_background):
    """Test horizontal lines of different lengths and thickness."""
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    Line(vertices=(Vec2D(-40, -45), Vec2D(40, -45))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-30, -35), Vec2D(40, -35))).draw(turtle, size=2)
    Line(vertices=(Vec2D(-30, -25), Vec2D(20, -25))).draw(turtle, size=4)
    Line(vertices=(Vec2D(-10, -10), Vec2D(20, -10))).draw(turtle, size=8)

    Line(vertices=(Vec2D(-10, 10), Vec2D(10, 10))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-20, 15), Vec2D(20, 15))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-30, 20), Vec2D(30, 20))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-40, 25), Vec2D(40, 25))).draw(turtle, size=1)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path("tests/component/lines/expected_horizontal_lines.png")
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
