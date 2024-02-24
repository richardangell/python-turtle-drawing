from turtle import Turtle, Vec2D
from helpers import jump_to


class Diamond:
    """Class for drawing a diamond shape."""

    def __init__(self, origin: Vec2D):
        self.origin = origin

    def draw(self, turtle: Turtle, fill: bool = False, colour: str = "black"):
        """Draw the diamond shape.

        Args:
            turtle (Turtle): turtle to draw with.
            fill (bool): whether to fill the shape with colour.
            colour (str): colour to use for the shape.

        """
        jump_to(turtle, self.origin)

        original_colour = turtle.pencolor()
        turtle.color(colour)

        if fill:
            turtle.begin_fill()

        turtle.setheading(45)
        for _ in range(4):
            turtle.forward(20)
            turtle.left(90)

        if fill:
            turtle.end_fill()

        turtle.color(original_colour)
