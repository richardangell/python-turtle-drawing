from turtle import Screen, Vec2D, Turtle
import turtle as t
import argparse

import numpy as np

from diamond import Diamond
from line import draw_curved_line, OffsetFromLine


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q", "--quick", action="store_true", help="render image quickly"
    )
    args = parser.parse_args()

    turtle_ = Turtle()

    if args.quick:
        t.tracer(0, 0)

    s1 = Vec2D(0, 0)
    s2 = Vec2D(-100, 100)
    s3 = Vec2D(0, 200)
    s4 = Vec2D(100, 100)
    s5 = Vec2D(0, 0)

    turtle_.begin_fill()

    draw_curved_line(turtle_, s1, s2, OffsetFromLine(offset=20), steps=20)
    draw_curved_line(turtle_, s2, s3, OffsetFromLine(offset=10), steps=20)
    draw_curved_line(turtle_, s3, s4, OffsetFromLine(offset=15), steps=20)
    draw_curved_line(turtle_, s4, s1, OffsetFromLine(offset=20), steps=20)

    turtle_.end_fill()

    mult = 1

    for x in np.linspace(-100, 100, 11):
        for y in np.linspace(-100, 100, 11):
            Diamond(Vec2D(x + (mult * 10), y)).draw(turtle_, fill=True, colour="white")

            mult *= -1

    draw_curved_line(turtle_, s1, s2, OffsetFromLine(offset=20), steps=20)
    draw_curved_line(turtle_, s2, s3, OffsetFromLine(offset=10), steps=20)
    draw_curved_line(turtle_, s3, s4, OffsetFromLine(offset=15), steps=20)
    draw_curved_line(turtle_, s4, s1, OffsetFromLine(offset=20), steps=20)

    if args.quick:
        t.update()

    screen = Screen()
    screen.exitonclick()
