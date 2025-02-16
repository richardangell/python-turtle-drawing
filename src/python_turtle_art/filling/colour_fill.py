from turtle import Turtle

from .base_fill import BaseFill


class ColourFill(BaseFill):
    def __init__(self, fill_colour="black"):
        self.fill_colour = fill_colour

    def pre_draw(self, turtle: Turtle):
        self._original_fill_colour = turtle.fillcolor()
        turtle.fillcolor(self.fill_colour)
        turtle.begin_fill()

    def post_draw(self, turtle: Turtle):
        turtle.end_fill()
        turtle.fillcolor(self._original_fill_colour)
