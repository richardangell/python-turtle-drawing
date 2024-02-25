from turtle import Turtle, Vec2D
from typing import Optional
from abc import ABC, abstractmethod

from helpers import jump_to
from line import draw_curved_line, OffsetFromLine


class Eyes:
    """Class for drawing simple eyes."""

    def __init__(
        self,
        left_eye: Vec2D,
        right_eye: Vec2D,
        left_eye_size: Optional[int] = None,
        right_eye_size: Optional[int] = None,
    ):
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.left_eye_size = left_eye_size
        self.right_eye_size = right_eye_size

    def draw(self, turtle: Turtle):
        jump_to(turtle, self.left_eye)
        turtle.dot(self.left_eye_size)

        jump_to(turtle, self.right_eye)
        turtle.dot(self.right_eye_size)


class Mouth(ABC):
    @abstractmethod
    def draw(self, turtle: Turtle):
        raise NotImplementedError


class RoundMouth(Mouth):
    def __init__(self, location: Vec2D, size: Optional[int] = None):
        self.location = location
        self.size = size

    def draw(self, turtle: Turtle):
        jump_to(turtle, self.location)
        turtle.dot(self.size)


class CurvedMouth(Mouth):
    def __init__(
        self,
        start: Vec2D,
        end: Vec2D,
        off_line: OffsetFromLine = OffsetFromLine(),
        size: Optional[int] = None,
    ):
        self.start = start
        self.end = end
        self.off_line = off_line
        self.size = size

    def draw(self, turtle: Turtle):
        jump_to(turtle, self.start)

        draw_curved_line(
            turtle=turtle,
            start=self.start,
            end=self.end,
            off_line=self.off_line,
            steps=10,
            draw_points=False,
            size=self.size,
        )
