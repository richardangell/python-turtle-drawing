from turtle import Turtle

from .base_fill import BaseFill


class ColourFill(BaseFill):
    def __init__(self, fillcolour="black"):
        self.fillcolour = fillcolour

    def pre_draw(self, turtle: Turtle):
        self._original_colour = turtle.pencolor()
        turtle.color(self.fillcolour)
        turtle.begin_fill()

    def post_draw(self, turtle: Turtle):
        turtle.end_fill()
        turtle.color(self._original_colour)
