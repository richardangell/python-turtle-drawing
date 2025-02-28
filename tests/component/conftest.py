from turtle import RawTurtle, TurtleScreen, Vec2D
from typing import Any, Generator

import pytest

from python_turtle_art.cli import setup_turtle_and_screen
from python_turtle_art.filling import ColourFill
from python_turtle_art.helpers.turtle import turn_off_turtle_animation, update_screen
from python_turtle_art.polygons.kites.convex_kite import ConvexKite


@pytest.fixture
def setup_screen_with_squares_background(
    request,
) -> Generator[tuple[RawTurtle, TurtleScreen], Any, None]:
    """Set up turtle Screen and Turtle objects.

    Screen is set to the requested height and width. This fixture should be
    parametrized with a tuple of height and width ints.

    """

    window_dimensions, screen_dimensions = request.param
    turtle, screen = setup_turtle_and_screen(
        window_dimensions=window_dimensions, screen_dimensions=screen_dimensions
    )
    turtle.hideturtle()
    turn_off_turtle_animation(screen)

    draw_grey_squares_on_yellow_background(turtle)

    yield turtle, screen

    update_screen(screen)
    screen.clearscreen()


def draw_grey_squares_on_yellow_background(turtle: RawTurtle) -> None:
    """Draw four grey squares on a yellow background."""

    background_square = ConvexKite(
        vertices=(Vec2D(-50, -50), Vec2D(50, -50), Vec2D(50, 50), Vec2D(-50, 50))
    )
    background_square.draw(turtle, size=0.5)
    background_square.fill(turtle, ColourFill("yellow"))

    # bottom left
    l = -49
    u = -2
    kite = ConvexKite(vertices=(Vec2D(l, l), Vec2D(u, l), Vec2D(u, u), Vec2D(l, u)))
    kite.draw(turtle, size=0.5, colour="grey")

    # top right
    l = 49
    u = 2
    kite = ConvexKite(vertices=(Vec2D(l, l), Vec2D(u, l), Vec2D(u, u), Vec2D(l, u)))
    kite.draw(turtle, size=0.5, colour="grey")

    # bottom right
    l = -49
    u = -2
    kite = ConvexKite(vertices=(Vec2D(-l, l), Vec2D(-l, u), Vec2D(-u, u), Vec2D(-u, l)))
    kite.draw(turtle, size=0.5, colour="grey")

    # top left
    l = -49
    u = -2
    kite = ConvexKite(vertices=(Vec2D(l, -l), Vec2D(l, -u), Vec2D(u, -u), Vec2D(u, -l)))
    kite.draw(turtle, size=0.5, colour="grey")
