from abc import ABC, abstractmethod
from turtle import Turtle


class BaseFill(ABC):
    @abstractmethod
    def pre_draw(self, turtle: Turtle):
        """Pre edge-drawing step."""
        raise NotImplementedError

    @abstractmethod
    def post_draw(self, turtle: Turtle):
        """Post edge-drawing step."""
        raise NotImplementedError


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
