from argparse import Namespace, ArgumentParser
from turtle import Turtle, Screen, _Screen
from datetime import datetime

from .pine_cones import helpers
from .write import save_turtle_screen
from .pine_cones.main import draw_image


def setup_turtle_and_screen(height: int, width: int) -> tuple[Turtle, _Screen]:
    """Create Turtle and Screen objects."""

    turtle_ = Turtle()
    screen = Screen()
    screen.screensize(height, width)

    return turtle_, screen


class CommandLineArguments(Namespace):
    """Class to hold command line arguments."""

    quick: bool
    no_turtle: bool
    exit_on_click: bool
    save_image: bool
    screen_height: int
    screen_width: int


def run():
    """Function run by the python_turtle_drawing command."""

    parser = ArgumentParser()
    parser.add_argument(
        "-q", "--quick", action="store_true", help="render image quickly"
    )
    parser.add_argument("-n", "--no_turtle", action="store_true", help="hide turtle")
    parser.add_argument(
        "-e", "--exit_on_click", action="store_true", help="exit turtle screen on click"
    )
    parser.add_argument(
        "-s", "--save_image", action="store_true", help="save image to jpeg"
    )
    parser.add_argument(
        "--screen_height", action="store", type=int, default=4000, help="screen height"
    )
    parser.add_argument(
        "--screen_width", action="store", type=int, default=4000, help="screen width"
    )
    args = parser.parse_args(namespace=CommandLineArguments)

    turtle_, screen = setup_turtle_and_screen(args.screen_height, args.screen_width)

    if args.no_turtle:
        turtle_.hideturtle()

    if args.quick:
        helpers.turn_off_turtle_animation()

    draw_image(turtle=turtle_)

    if args.quick:
        helpers.update_screen()

    if args.save_image:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_turtle_screen(
            canvas=screen.getcanvas(),  # type: ignore
            file=f"img {timestamp}.jpeg",
            height=args.screen_height,
            width=args.screen_width,
        )

    if args.exit_on_click:
        screen.exitonclick()
