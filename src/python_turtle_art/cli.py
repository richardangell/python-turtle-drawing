from argparse import ArgumentParser, Namespace
from datetime import datetime
from turtle import Screen, Turtle, _Screen

from .drawings import draw_image_pine_cones, draw_image_stars_3bp
from .helpers.turtle import turn_off_turtle_animation, update_screen
from .write import save_turtle_screen

MODULE_DRAW_FUNCTION_MAPPING = {
    "pine_cones": draw_image_pine_cones,
    "stars_3bp": draw_image_stars_3bp,
}


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
    drawing: str


def parse_arguments():
    """Parse command line arguments."""

    parser = ArgumentParser()
    parser.add_argument(
        "-q", "--quick", action="store_true", help="Render the image quickly."
    )
    parser.add_argument(
        "-n",
        "--no_turtle",
        action="store_true",
        help="Hide the turtle while the image is being drawn.",
    )
    parser.add_argument(
        "-e",
        "--exit_on_click",
        action="store_true",
        help="Keep the screen open and only exit screen on click.",
    )
    parser.add_argument(
        "-s",
        "--save_image",
        action="store_true",
        help="Save image to png. File will be timestamped.",
    )
    parser.add_argument(
        "--screen_height",
        action="store",
        type=int,
        default=4000,
        help="The screen height.",
    )
    parser.add_argument(
        "--screen_width",
        action="store",
        type=int,
        default=4000,
        help="The screen width.",
    )
    parser.add_argument(
        "-d",
        "--drawing",
        action="store",
        type=str,
        default="pine_cones",
        help="The name of the drawing to produce.",
    )

    return parser.parse_args(namespace=CommandLineArguments)


def run():
    """Function run by the python_turtle_drawing command."""

    args = parse_arguments()

    turtle_, screen = setup_turtle_and_screen(args.screen_height, args.screen_width)

    if args.no_turtle:
        turtle_.hideturtle()

    if args.quick:
        turn_off_turtle_animation()

    drawing_function = MODULE_DRAW_FUNCTION_MAPPING[args.drawing]

    drawing_function(turtle=turtle_)

    if args.quick:
        update_screen()

    if args.save_image:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_turtle_screen(
            canvas=screen.getcanvas(),  # type: ignore
            file=f"img {timestamp}.png",
            height=args.screen_height,
            width=args.screen_width,
        )

    if args.exit_on_click:
        screen.exitonclick()
