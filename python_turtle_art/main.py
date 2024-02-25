from turtle import Screen, Vec2D, Turtle
import argparse

import numpy as np

from kite import ConvexKite, CurvedConvexKite, CurvedConvexKiteFactory
from line import draw_curved_line, OffsetFromLine
from face import Eyes, RoundMouth, CurvedMouth
from body_parts import Extremity
import helpers
from pine_cone import PineCone


def _aaa():
    """WIP function, overlays kites over curved kite."""

    s1 = Vec2D(0, 0)
    s2 = Vec2D(-100, 100)
    s3 = Vec2D(0, 200)
    s4 = Vec2D(100, 100)

    mult = 1

    for x in np.linspace(-100, 100, 11):
        for y in np.linspace(-100, 100, 11):
            ConvexKite(origin=Vec2D(x + (mult * 10), y), height=30, width=20).draw(
                turtle_, fill=True, colour="white"
            )

            mult *= -1

    draw_curved_line(turtle_, s1, s2, OffsetFromLine(offset=20), steps=20)
    draw_curved_line(turtle_, s2, s3, OffsetFromLine(offset=10), steps=20)
    draw_curved_line(turtle_, s3, s4, OffsetFromLine(offset=15), steps=20)
    draw_curved_line(turtle_, s4, s1, OffsetFromLine(offset=20), steps=20)


def main(turtle: Turtle):
    """Main drawing function."""

    s1 = Vec2D(0, 0)

    rotation = 10

    outer_kite = CurvedConvexKite(
        origin=s1,
        off_lines=(
            OffsetFromLine(offset=50),
            OffsetFromLine(offset=10),
            OffsetFromLine(offset=15),
            OffsetFromLine(offset=50),
        ),
        height=300,
        width=200,
        diagonal_intersection_along_height=0.4,
        rotation=rotation,
    )

    inner_kite_factor = CurvedConvexKiteFactory(
        off_lines=(
            OffsetFromLine(offset=3),
            OffsetFromLine(offset=-3),
            OffsetFromLine(offset=-3),
            OffsetFromLine(offset=3),
        ),
        height=70,
        width=60,
        diagonal_intersection_along_height=0.45,
        rotation=rotation + 2,
        rotation_point=s1,
    )

    CurvedMouth(
        start=helpers.rotate_about_point(Vec2D(-20, 20), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(-25, -100), rotation, s1),
        off_line=OffsetFromLine(0.8, -10),
        size=8,
    ).draw(turtle)

    CurvedMouth(
        start=helpers.rotate_about_point(Vec2D(15, 20), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(35, -95), rotation, s1),
        off_line=OffsetFromLine(0.7, 10),
        size=8,
    ).draw(turtle)

    PineCone(outer_kite=outer_kite, inner_kite_factory=inner_kite_factor).draw(
        turtle=turtle
    )

    Eyes(
        left_eye=helpers.rotate_about_point(Vec2D(-20, 230), rotation, s1),
        right_eye=helpers.rotate_about_point(Vec2D(20, 230), rotation, s1),
        left_eye_size=15,
        right_eye_size=25,
    ).draw(turtle)

    RoundMouth(
        location=helpers.rotate_about_point(Vec2D(0, 180), rotation, s1), size=35
    ).draw(turtle)

    # CurvedMouth(
    #    start=helpers.rotate_about_point(Vec2D(-20, 180), rotation, s1),
    #    end=helpers.rotate_about_point(Vec2D(20, 180), rotation, s1),
    #    off_line=OffsetFromLine(0.8, -40),
    #    size = 12
    # ).draw(turtle)

    Extremity(
        start=helpers.rotate_about_point(Vec2D(-80, 160), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(-90, 180), rotation, s1),
        off_line=OffsetFromLine(0.8, -10),
        size=8,
    ).draw(turtle)

    Extremity(
        start=helpers.rotate_about_point(Vec2D(90, 160), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(95, 180), rotation, s1),
        off_line=OffsetFromLine(0.7, 10),
        size=8,
    ).draw(turtle)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q", "--quick", action="store_true", help="render image quickly"
    )
    args = parser.parse_args()

    turtle_ = Turtle()

    if args.quick:
        helpers.turn_off_turtle_animation()

    turtle_.hideturtle()

    main(turtle_)

    if args.quick:
        helpers.update_screen()

    screen = Screen()
    screen.exitonclick()
