from turtle import Turtle

from ..helpers.turtle import jump_to
from ..polygons.convex_polygon import ConvexPolygon
from ..polygons.polygon import BaseFill, Polygon


class ColourFill(BaseFill):
    def __init__(self, fill_colour="black"):
        self.fill_colour = fill_colour

    def fill(self, turtle: Turtle, polygon: Polygon | ConvexPolygon):
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
