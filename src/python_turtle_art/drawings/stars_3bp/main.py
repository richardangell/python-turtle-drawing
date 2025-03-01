from turtle import RawTurtle, Vec2D

from ...filling import ColourFill, HashFill
from ...helpers.turtle import jump_to
from ...lines.offset_from_line import OffsetFromLine
from ...polygons.kites.convex_curved_kite import ConvexCurvedKite
from ...polygons.kites.convex_kite import ConvexKite


def draw_background(turtle: RawTurtle) -> None:
    kite = ConvexKite(
        vertices=(
            Vec2D(200, -1000),
            Vec2D(2200, -1000),
            Vec2D(2200, -2200),
            Vec2D(200, -2200),
        )
    )
    cross_fill = HashFill(gap=6, origin=0, size=4)

    kite.draw(turtle, size=5)
    kite.fill(turtle, cross_fill)


def draw_circle_in_kite_centre(
    turtle: RawTurtle, kite_origin: Vec2D, kite_height: int | float, radius: int
) -> None:
    centre_kite = kite_origin + Vec2D(0, kite_height / 2)
    bottom_circle = centre_kite + Vec2D(0, -radius)

    jump_to(turtle, bottom_circle)
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.pensize(5)
    turtle.circle(radius=radius)
    turtle.end_fill()


def draw_image(turtle: RawTurtle):
    draw_background(turtle)

    kite = ConvexKite.from_origin_and_dimensions(
        origin=Vec2D(500, -2000),
        height=200,
        width=200,
        diagonal_intersection_along_height=0.5,
    )

    white_fill = ColourFill(fill_colour="white")
    cross_fill = HashFill(gap=6, origin=0, size=1)

    kite.fill(turtle, white_fill)
    kite.draw(turtle, size=5)
    kite.fill(turtle, cross_fill)

    draw_circle_in_kite_centre(
        turtle=turtle,
        kite_origin=Vec2D(500, -2000),
        kite_height=200,
        radius=50,
    )

    kite2 = ConvexCurvedKite.from_origin_and_dimensions(
        origin=Vec2D(1000, -2000),
        height=400,
        width=400,
        diagonal_intersection_along_height=0.5,
        off_lines=(
            OffsetFromLine(offset=5),
            OffsetFromLine(offset=5),
            OffsetFromLine(offset=5),
            OffsetFromLine(offset=5),
        ),
    )

    kite2.fill(turtle, white_fill)
    kite2.draw(turtle, size=5)
    kite2.fill(turtle, cross_fill)

    draw_circle_in_kite_centre(
        turtle=turtle,
        kite_origin=Vec2D(1000, -2000),
        kite_height=400,
        radius=80,
    )

    kite3 = ConvexCurvedKite.from_origin_and_dimensions(
        origin=Vec2D(750, -1750),
        height=370,
        width=370,
        diagonal_intersection_along_height=0.5,
        off_lines=(
            OffsetFromLine(offset=5),
            OffsetFromLine(offset=5),
            OffsetFromLine(offset=5),
            OffsetFromLine(offset=5),
        ),
    )

    kite3.fill(turtle, white_fill)
    kite3.draw(turtle, size=5)
    kite3.fill(turtle, cross_fill)

    draw_circle_in_kite_centre(
        turtle=turtle,
        kite_origin=Vec2D(750, -1750),
        kite_height=370,
        radius=80,
    )

    turtle.pensize(1)
    turtle.pencolor("white")
    turtle.goto(2200, -2200)
