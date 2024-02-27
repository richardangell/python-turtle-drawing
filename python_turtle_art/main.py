from turtle import Screen, Vec2D, Turtle
import argparse
import turtle as t

import numpy as np

from kite import CurvedConvexKite, CurvedConvexKiteFactory
from line import OffsetFromLine
from face import Eyes, CurvedMouth
from body import Limb
import helpers
from pine_cone import PineCone, RandomPineConeFactory
from write import save_turtle_screen

SCREEN_SIZE = (4000, 4000)


def draw_background_characters(turtle: Turtle):
    """Main drawing function."""

    characters_in_row = 10
    n_rows = 7
    horizontal_character_offset = 300
    vertical_character_offset = 500

    rotation_range_signs = [1, 1, -1, -1, 1, 1, -1]
    rotation_range_increment = 5
    start_rotation_ranges = [
        (0, 10),
        (-45, -35),
        (0, 10),
        (35, 45),
        (0, 10),
        (-45, -35),
        (0, 10),
    ]

    for row_number in reversed(range(n_rows)):
        y = -row_number * vertical_character_offset

        character_counter = 0

        start_rotation_range = start_rotation_ranges[row_number]
        rotation_range_sign = rotation_range_signs[row_number]

        for x in np.linspace(
            0, characters_in_row * horizontal_character_offset, characters_in_row
        ):
            p1 = Vec2D(x, y)

            rotation_range = (
                start_rotation_range[0]
                + rotation_range_sign * character_counter * rotation_range_increment,
                start_rotation_range[1]
                + rotation_range_sign * character_counter * rotation_range_increment,
            )

            random_pine_cone = RandomPineConeFactory(
                origin=p1,
                height_range=(300, 350),
                rotation_range=rotation_range,
                seed=None,
                verbose=False,
            ).create()

            random_pine_cone.draw(turtle)

            character_counter += 1

            helpers.update_screen()


def draw_main_character(turtle: Turtle):
    """Draw specific character."""

    s1 = Vec2D(1000, -1600)

    rotation = 10

    outer_kite = CurvedConvexKite(
        origin=s1,
        off_lines=(
            OffsetFromLine(offset=50),
            OffsetFromLine(offset=10),
            OffsetFromLine(offset=15),
            OffsetFromLine(offset=50),
        ),
        height=1200,
        width=800,
        diagonal_intersection_along_height=0.45,
        rotation=rotation,
    )

    inner_kite_factor = CurvedConvexKiteFactory(
        off_lines=(
            OffsetFromLine(offset=12),
            OffsetFromLine(offset=-12),
            OffsetFromLine(offset=-12),
            OffsetFromLine(offset=12),
        ),
        height=120,
        width=240,
        diagonal_intersection_along_height=0.45,
        rotation=rotation + 2,
        rotation_point=s1,
    )

    left_leg = Limb(
        start=helpers.rotate_about_point(s1 + Vec2D(-80, 80), rotation, s1),
        end=helpers.rotate_about_point(s1 + Vec2D(-100, -400), rotation, s1),
        off_line=OffsetFromLine(0.8, -40),
        size=32,
    )

    right_leg = Limb(
        start=helpers.rotate_about_point(s1 + Vec2D(60, 80), rotation, s1),
        end=helpers.rotate_about_point(s1 + Vec2D(140, -380), rotation, s1),
        off_line=OffsetFromLine(0.7, 40),
        size=32,
    )

    eyes = Eyes(
        left_eye=helpers.rotate_about_point(s1 + Vec2D(-80, 920), rotation, s1),
        right_eye=helpers.rotate_about_point(s1 + Vec2D(80, 920), rotation, s1),
        left_eye_size=60,
        right_eye_size=100,
    )

    mouth = CurvedMouth(
        start=helpers.rotate_about_point(s1 + Vec2D(-80, 720), rotation, s1),
        end=helpers.rotate_about_point(s1 + Vec2D(80, 720), rotation, s1),
        off_line=OffsetFromLine(0.8, -80),
        size=48,
    )

    left_arm = Limb(
        start=helpers.rotate_about_point(s1 + Vec2D(-320, 640), rotation, s1),
        end=helpers.rotate_about_point(s1 + Vec2D(-360, 720), rotation, s1),
        off_line=OffsetFromLine(0.8, -40),
        size=32,
        outline=False,
    )

    right_arm = Limb(
        start=helpers.rotate_about_point(s1 + Vec2D(360, 640), rotation, s1),
        end=helpers.rotate_about_point(s1 + Vec2D(380, 720), rotation, s1),
        off_line=OffsetFromLine(0.7, 40),
        size=32,
        outline=False,
    )

    pine_cone = PineCone(
        outer_kite=outer_kite,
        inner_kite_factory=inner_kite_factor,
        outer_kite_line_width=20,
        horizontal_offset=20,
        vertical_offset=20,
        initial_body_parts=(left_leg, right_leg),
        final_body_parts=(eyes, mouth, left_arm, right_arm),
    )

    pine_cone.draw(turtle=turtle)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q", "--quick", action="store_true", help="render image quickly"
    )
    args = parser.parse_args()

    turtle_ = Turtle()

    t.screensize(*SCREEN_SIZE)

    if args.quick:
        helpers.turn_off_turtle_animation()

    turtle_.hideturtle()

    draw_main_character(turtle_)
    draw_background_characters(turtle_)

    if args.quick:
        helpers.update_screen()

    screen = Screen()

    save_turtle_screen(
        canvas=screen.getcanvas(),  # type: ignore
        file="img.jpeg",
        height=SCREEN_SIZE[0],
        width=SCREEN_SIZE[1],
    )

    # screen.exitonclick()
