from pathlib import Path
from turtle import Vec2D

import pytest
from PIL import Image

from python_turtle_art.lines import OffsetFromLine, QuadraticBezierCurve
from python_turtle_art.write import get_canvas_image

from ...helpers import assert_image_difference_within_tolerance


@pytest.mark.window_dimensions((100, 100))
def test_control_point_after_line_end_point(setup_screen_with_squares_background):
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(30, 40),
        end=Vec2D(30, 10),
        off_line=OffsetFromLine(2.5, -100),
    ).draw(turtle, size=3)

    # Assert

    actual_image = get_canvas_image(screen, 100, 100, True)

    expected_image_file = Path(
        "tests/component/lines/expected_control_point_after_line_end.png"
    )
    expected_image = Image.open(expected_image_file)

    assert_image_difference_within_tolerance(
        actual=actual_image,
        expected=expected_image,
        tolerance_non_matching_pixels=0,
        tolerance_adjacent_pixels=0,
    )


@pytest.mark.window_dimensions((100, 100))
def test_increasing_distance_of_control_point_from_line(
    setup_screen_with_squares_background,
):
    # Arrange

    turtle, screen = setup_screen_with_squares_background

    # Act
    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-30, -30),
        end=Vec2D(30, 30),
        off_line=OffsetFromLine(0.3, 10),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-30, -30),
        end=Vec2D(30, 30),
        off_line=OffsetFromLine(0.3, 20),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-30, -30),
        end=Vec2D(30, 30),
        off_line=OffsetFromLine(0.3, 30),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-30, -30),
        end=Vec2D(30, 30),
        off_line=OffsetFromLine(0.3, 40),
    ).draw(turtle, size=1)

    QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(-10, -25),
        end=Vec2D(30, -25),
        off_line=OffsetFromLine(0.7, -30),
    ).draw(turtle, size=2)

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
