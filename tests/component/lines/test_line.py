from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.lines import Line
from python_turtle_art.write import get_canvas_image

from ...helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_line(setup_screen_with_squares_background):
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    # vertical lines
    Line(vertices=(Vec2D(-40, 10), Vec2D(-40, 40))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-35, 10), Vec2D(-35, 40))).draw(turtle, size=2)
    Line(vertices=(Vec2D(-25, 10), Vec2D(-25, 40))).draw(turtle, size=4)

    # diagonal (45 degrees) lines
    Line(vertices=(Vec2D(-40, -40), Vec2D(40, 40))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-30, -40), Vec2D(40, 30))).draw(turtle, size=1)
    Line(vertices=(Vec2D(-20, -40), Vec2D(40, 20))).draw(turtle, size=1)

    # horizontal lines
    Line(vertices=(Vec2D(10, -45), Vec2D(40, -45))).draw(turtle, size=1)
    Line(vertices=(Vec2D(20, -35), Vec2D(40, -35))).draw(turtle, size=2)
    Line(vertices=(Vec2D(20, -25), Vec2D(40, -25))).draw(turtle, size=4)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100)

    expected_image_file = Path("tests/component/lines/expected_lines.png")
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
