import tkinter as tk
import warnings
from argparse import ArgumentParser, Namespace
from datetime import datetime
from turtle import RawTurtle, TurtleScreen

from .draw import draw_image
from .drawings import draw_image_pine_cones, draw_image_stars_3bp
from .helpers.turtle import turn_off_turtle_animation, update_screen
from .write import save_turtle_screen

MODULE_DRAW_FUNCTION_MAPPING = {
    "pine_cones": draw_image_pine_cones,
    "stars_3bp": draw_image_stars_3bp,
    "draw": draw_image,
}


def setup_turtle_and_screen(
    window_dimensions: tuple[int | float, int | float] | None,
    screen_dimensions: tuple[int, int] | None,
) -> tuple[RawTurtle, TurtleScreen]:
    """Create Turtle and Screen objects.

    Args:
        window_dimensions (tuple[int, int]): The width and height of the main window.
            Values are passed to the turtle.setup() function.
        screen_dimensions (tuple[int, int]): The width and height of the screen. Values
            are passed to the Screen.screensize() function.

    """

    # if window_dimensions is None:
    #    setup()
    # else:
    #    setup(width=window_dimensions[0], height=window_dimensions[1])

    root = tk.Tk()
    # root.tk.call("tk", "scaling", 2)
    if window_dimensions is not None:
        canvas = tk.Canvas(
            root,
            width=window_dimensions[0],
            height=window_dimensions[1],
            borderwidth=0,
            highlightthickness=0,
            insertwidth=0,
            selectborderwidth=0,
        )
        print(canvas.winfo_reqwidth(), canvas.winfo_reqheight())
        canvas.pack()
    else:
        raise ValueError("window_dimensions must be provided")

    screen = TurtleScreen(canvas)

    l = 100
    # screen.setworldcoordinates(-l, -l, l, l)

    # screen = Screen()

    # if screen_dimensions is not None:
    #    screen.screensize(screen_dimensions[0], screen_dimensions[1])

    turtle_ = RawTurtle(screen)
    # turtle_ = Turtle()

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

    # 200 x 200 = 202 x 201 pixels, blank boarder: top, left, rifght
    # 198 x 198 = 200 x 199 pixels, blank boarder: top, left, rifght
    parser.add_argument(
        "-he",
        "--screen_height",
        action="store",
        type=int,
        default=100,
        help="The screen height.",
    )
    parser.add_argument(
        "-w",
        "--screen_width",
        action="store",
        type=int,
        default=100,
        help="The screen width.",
    )
    parser.add_argument(
        "-d",
        "--drawing",
        action="store",
        type=str,
        default="draw",
        help="The name of the drawing to produce.",
    )

    return parser.parse_args(namespace=CommandLineArguments)


def run():
    """Function run by the python_turtle_drawing command."""

    args = parse_arguments()

    turtle, screen = setup_turtle_and_screen(
        window_dimensions=(args.screen_width, args.screen_height),
        screen_dimensions=(args.screen_width, args.screen_height),
    )

    if args.no_turtle:
        turtle.hideturtle()

    if args.quick:
        turn_off_turtle_animation(screen)

    drawing_function = MODULE_DRAW_FUNCTION_MAPPING[args.drawing]

    drawing_function(turtle=turtle)

    if args.quick:
        update_screen(screen)

    if args.save_image:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_turtle_screen(
            screen=screen,
            file=f"img {timestamp}.png",
            height=args.screen_height,
            width=args.screen_width,
        )

    if args.exit_on_click:
        warnings.warn("exit_on_click not implemented")
