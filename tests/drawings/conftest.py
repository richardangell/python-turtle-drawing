import turtle
from typing import Any, Generator

import pytest

from python_turtle_art.cli import setup_turtle_and_screen


@pytest.fixture
def setup_screen(request) -> Generator[tuple[turtle.Turtle, turtle._Screen], Any, None]:
    """Set up turtle Screen and Turtle objects.

    Screen is set to the requested height and width. This fixture should be
    parametrized with a tuple of height and width ints.

    """

    window_dimensions, screen_dimensions = request.param
    turtle_, screen = setup_turtle_and_screen(
        window_dimensions=window_dimensions, screen_dimensions=screen_dimensions
    )
    turtle_.hideturtle()

    yield turtle_, screen

    turtle.clearscreen()
