from turtle import Screen, Vec2D, Turtle
import argparse

from kite import CurvedConvexKite, CurvedConvexKiteFactory
from line import OffsetFromLine
from face import Eyes, CurvedMouth
from body import Limb
import helpers
from pine_cone import PineCone, RandomPineConeFactory


def main(turtle: Turtle):
    """Main drawing function."""

    random_pine_cone = RandomPineConeFactory(
        origin=Vec2D(-50, -50), height_range=(300, 350), seed=None, verbose=True
    ).create()

    random_pine_cone.draw(turtle)


def draw_pine_cone(turtle: Turtle):
    """Draw specific character."""

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
        diagonal_intersection_along_height=0.45,
        rotation=rotation,
    )

    inner_kite_factor = CurvedConvexKiteFactory(
        off_lines=(
            OffsetFromLine(offset=3),
            OffsetFromLine(offset=-3),
            OffsetFromLine(offset=-3),
            OffsetFromLine(offset=3),
        ),
        height=30,
        width=60,
        diagonal_intersection_along_height=0.45,
        rotation=rotation + 2,
        rotation_point=s1,
    )

    left_arm = Limb(
        start=helpers.rotate_about_point(Vec2D(-20, 20), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(-25, -100), rotation, s1),
        off_line=OffsetFromLine(0.8, -10),
        size=8,
    )

    right_arm = Limb(
        start=helpers.rotate_about_point(Vec2D(15, 20), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(35, -95), rotation, s1),
        off_line=OffsetFromLine(0.7, 10),
        size=8,
    )

    eyes = Eyes(
        left_eye=helpers.rotate_about_point(Vec2D(-20, 230), rotation, s1),
        right_eye=helpers.rotate_about_point(Vec2D(20, 230), rotation, s1),
        left_eye_size=15,
        right_eye_size=25,
    )

    # mouth = RoundMouth(
    #    location=helpers.rotate_about_point(Vec2D(0, 180), rotation, s1), size=35
    # )

    mouth = CurvedMouth(
        start=helpers.rotate_about_point(Vec2D(-20, 180), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(20, 180), rotation, s1),
        off_line=OffsetFromLine(0.8, -40),
        size=12,
    )

    left_leg = Limb(
        start=helpers.rotate_about_point(Vec2D(-80, 160), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(-90, 180), rotation, s1),
        off_line=OffsetFromLine(0.8, -10),
        size=8,
    )

    right_leg = Limb(
        start=helpers.rotate_about_point(Vec2D(90, 160), rotation, s1),
        end=helpers.rotate_about_point(Vec2D(95, 180), rotation, s1),
        off_line=OffsetFromLine(0.7, 10),
        size=8,
    )

    pine_cone = PineCone(
        outer_kite=outer_kite,
        inner_kite_factory=inner_kite_factor,
        initial_body_parts=(left_arm, right_arm),
        final_body_parts=(eyes, mouth, left_leg, right_leg),
    )

    pine_cone.draw(turtle=turtle)


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
