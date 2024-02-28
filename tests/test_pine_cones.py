from python_turtle_drawing.pine_cones.main import draw_image
from python_turtle_drawing.cli import setup_turtle_and_screen
from python_turtle_drawing.write import get_canvas_image
from python_turtle_drawing.pine_cones import helpers

from pathlib import Path

from PIL import Image, ImageChops


def test_image_produced():
    """Check pine_cones.main.draw_image produces the expected image."""

    expected_image_file = Path("tests/pine_cones.png")
    expected_image = Image.open(expected_image_file)

    height, width = 4000, 4000
    turtle_, screen = setup_turtle_and_screen(height, width)
    turtle_.hideturtle()

    helpers.turn_off_turtle_animation()
    draw_image(turtle_)
    helpers.update_screen()

    actual_image = get_canvas_image(screen.getcanvas(), height, width)

    difference = ImageChops.difference(actual_image, expected_image)

    assert (
        not difference.getbbox()
    ), "pine_cones.main.draw_image does not produce the expected image"
