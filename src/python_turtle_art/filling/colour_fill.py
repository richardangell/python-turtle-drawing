from turtle import Turtle, Vec2D

from ..helpers.turtle import jump_to
from .base_fill import BaseFill


class ColourFill(BaseFill):
    def __init__(self, fill_colour="black"):
        self.fill_colour = fill_colour

    def fill(self, turtle: Turtle, vertices: tuple[Vec2D, ...]):
        original_fill_colour = turtle.fillcolor()
        turtle.fillcolor(self.fill_colour)
        turtle.begin_fill()

        turtle.penup()

        jump_to(turtle=turtle, position=vertices[-1])
        for vertex in vertices:
            jump_to(turtle=turtle, position=vertex)

        turtle.pendown()

        turtle.end_fill()
        turtle.fillcolor(original_fill_colour)
