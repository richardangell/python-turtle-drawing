from turtle import Turtle, Vec2D

from ..fill import ColourFill
from ..kite import ConvexKite


def draw_image(turtle: Turtle):
    """Draw image."""

    kite = ConvexKite(
        origin=Vec2D(0, 0),
        height=400,
        width=300,
    )

    kite.draw(turtle, colour="red", fill=ColourFill(fillcolour="black"))

    kite.rotate(angle=30, about_point=Vec2D(0, 0)).draw(
        turtle, colour="red", fill=ColourFill(fillcolour="black")
    )

    turtle.circle(radius=40)
