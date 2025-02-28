from turtle import RawTurtle, TurtleScreen
from typing import Any, Generator

import pytest

from python_turtle_art.cli import setup_turtle_and_screen


@pytest.fixture
def setup_screen(request) -> Generator[tuple[RawTurtle, TurtleScreen], Any, None]:
    """Set up turtle Screen and Turtle objects.

    Screen is set to the requested height and width. This fixture should be
    parametrized with a tuple of height and width ints.

    """

    window_dimensions, screen_dimensions = request.param
    turtle, screen = setup_turtle_and_screen(
        window_dimensions=window_dimensions, screen_dimensions=screen_dimensions
    )
    turtle.hideturtle()

    yield turtle, screen

    screen.clearscreen()
