from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.lines import OffsetFromLine, QuadraticBezierCurve
from python_turtle_art.write import get_canvas_image

from ...helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_quadratic_bezier_curve(setup_screen_with_squares_background):
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-40, 10),
        end=Vec2D(-40, 40),
        off_line=OffsetFromLine(0.5, 10),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-30, 10),
        end=Vec2D(-30, 40),
        off_line=OffsetFromLine(0.5, 10),
    ).draw(turtle, size=2)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-5, 10),
        end=Vec2D(-5, 40),
        off_line=OffsetFromLine(0.3, 40),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-40, -40),
        end=Vec2D(40, 20),
        off_line=OffsetFromLine(0.8, 35),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(10, -10),
        end=Vec2D(40, -10),
        off_line=OffsetFromLine(0.8, -10),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(10, -30),
        end=Vec2D(40, -30),
        off_line=OffsetFromLine(0.2, 10),
    ).draw(turtle, size=3)

    # control point beyond the line end point
    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-5, -5),
        end=Vec2D(-5, -30),
        off_line=OffsetFromLine(1.5, -25),
    ).draw(turtle, size=1)

    # zero offset
    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(10, 40),
        end=Vec2D(40, 40),
        off_line=OffsetFromLine(1.5, 0),
    ).draw(turtle, size=1)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path(
        "tests/component/lines/expected_quadratic_beizer_curve.png"
    )
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )
