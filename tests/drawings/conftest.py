import turtle
from typing import Any, Generator

import pytest

from python_turtle_art.cli import setup_turtle_and_screen


@pytest.fixture
def setup_screen() -> Generator[tuple[turtle.Turtle, turtle._Screen], Any, None]:
    """Set up 400 x 400 screen."""

    height, width = 4000, 4000
    turtle_, screen = setup_turtle_and_screen(height, width)
    turtle_.hideturtle()

    yield turtle_, screen

    turtle.clearscreen()
