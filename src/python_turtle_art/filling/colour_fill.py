from turtle import RawTurtle

from ..helpers.turtle import jump_to
from ..polygons.polygon import Polygon
from .base_fill import BaseFill


class ColourFill(BaseFill):
    def __init__(self, fill_colour="black"):
        self.fill_colour = fill_colour

    def fill(self, turtle: RawTurtle, polygon: Polygon):
        original_fill_colour = turtle.fillcolor()
        turtle.fillcolor(self.fill_colour)
        turtle.begin_fill()

        turtle.penup()

        jump_to(turtle=turtle, position=polygon.vertices[-1])
        for vertex in polygon.vertices:
            jump_to(turtle=turtle, position=vertex)

        turtle.pendown()

        turtle.end_fill()
        turtle.fillcolor(original_fill_colour)
