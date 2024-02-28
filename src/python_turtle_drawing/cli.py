import argparse
from turtle import Turtle, Screen
import turtle as t

from .pine_cones import helpers
from .write import save_turtle_screen
from .pine_cones.main import draw_image


def run():
    parser = argparse.ArgumentParser()
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
    args = parser.parse_args()

    turtle_ = Turtle()

    if args.no_turtle:
        turtle_.hideturtle()

    t.screensize(args.screen_height, args.screen_width)

    if args.quick:
        helpers.turn_off_turtle_animation()

    draw_image(turtle=turtle_)

    if args.quick:
        helpers.update_screen()

    screen = Screen()

    if args.save_image:
        save_turtle_screen(
            canvas=screen.getcanvas(),  # type: ignore
            file="img.jpeg",
            height=args.screen_height,
            width=args.screen_width,
        )

    if args.exit_on_click:
        screen.exitonclick()
