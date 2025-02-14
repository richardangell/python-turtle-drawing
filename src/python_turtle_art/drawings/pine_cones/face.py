from abc import abstractmethod
from turtle import Turtle, Vec2D

from ...helpers.turtle import jump_to
from ...lines.offset_from_line import OffsetFromLine
from ...lines.quadratic_bezier_curve import draw_curved_line
from .body_part import BodyPart


class Eyes(BodyPart):
    """Class for drawing simple eyes."""

    def __init__(
        self,
        left_eye: Vec2D,
        right_eye: Vec2D,
        left_eye_size: int,
        right_eye_size: int,
    ):
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.left_eye_size = left_eye_size
        self.right_eye_size = right_eye_size

    def draw(self, turtle: Turtle):
        original_colour = turtle.pencolor()

        jump_to(turtle, self.left_eye)

        turtle.pencolor("white")
        turtle.dot(self.left_eye_size + 2)

        turtle.pencolor(original_colour)
        turtle.dot(self.left_eye_size)

        jump_to(turtle, self.right_eye)

        turtle.pencolor("white")
        turtle.dot(self.right_eye_size + 2)

        turtle.pencolor(original_colour)
        turtle.dot(self.right_eye_size)


class Mouth(BodyPart):
    @abstractmethod
    def draw(self, turtle: Turtle):
        raise NotImplementedError


class RoundMouth(Mouth):
    def __init__(self, location: Vec2D, size: int):
        self.location = location
        self.size = size

    def draw(self, turtle: Turtle):
        original_colour = turtle.pencolor()

        jump_to(turtle, self.location)

        turtle.pencolor("white")
        turtle.dot(self.size + 2)

        turtle.pencolor(original_colour)
        turtle.dot(self.size)


class CurvedMouth(Mouth):
    def __init__(
        self,
        start: Vec2D,
        end: Vec2D,
        size: int | float,
        off_line: OffsetFromLine | None = None,
        outline: bool = True,
    ):
        self.start = start
        self.end = end
        self.off_line = OffsetFromLine() if off_line is None else off_line
        self.size = size
        self.outline = outline

    def draw(self, turtle: Turtle):
        original_colour = turtle.pencolor()

        if self.outline:
            jump_to(turtle, self.start)

            turtle.pencolor("white")
            draw_curved_line(
                turtle=turtle,
                start=self.start,
                end=self.end,
                off_line=self.off_line,
                steps=10,
                draw_points=False,
                size=self.size + 2,
            )

        jump_to(turtle, self.start)

        turtle.pencolor(original_colour)
        draw_curved_line(
            turtle=turtle,
            start=self.start,
            end=self.end,
            off_line=self.off_line,
            steps=10,
            draw_points=False,
            size=self.size,
        )


class CurvedTriangleMouth(Mouth):
    def __init__(
        self,
        start: Vec2D,
        end: Vec2D,
        size: int,
        off_line: OffsetFromLine | None = None,
        fill: bool = True,
        colour: str = "white",
    ):
        self.start = start
        self.end = end
        self.off_line = OffsetFromLine() if off_line is None else off_line
        self.size = size
        self.fill = fill
        self.colour = colour

    def draw(self, turtle: Turtle):
        original_colour = turtle.pencolor()
        turtle.pencolor("white")

        jump_to(turtle, self.start)

        draw_curved_line(
            turtle=turtle,
            start=self.start,
            end=self.end,
            off_line=self.off_line,
            steps=10,
            draw_points=False,
            size=self.size + 2,
        )

        jump_to(turtle, self.end)

        draw_curved_line(
            turtle=turtle,
            start=self.end,
            end=self.start,
            off_line=self.off_line,
            steps=2,
            draw_points=False,
            size=self.size + 2,
        )

        turtle.pencolor(original_colour)

        if self.fill:
            turtle.fillcolor(self.colour)
            turtle.begin_fill()

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

        jump_to(turtle, self.end)

        draw_curved_line(
            turtle=turtle,
            start=self.end,
            end=self.start,
            off_line=self.off_line,
            steps=2,
            draw_points=False,
            size=self.size,
        )

        if self.fill:
            turtle.end_fill()
