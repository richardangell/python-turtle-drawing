from abc import abstractmethod
from turtle import Turtle, Vec2D

from ...fill import ColourFill
from ...helpers.turtle import jump_to
from ...lines.offset_from_line import OffsetFromLine
from ...lines.quadratic_bezier_curve import QuadraticBezierCurve
from ...polygons.polygon import Polygon
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
            QuadraticBezierCurve.from_start_and_end(
                start=self.start,
                end=self.end,
                off_line=self.off_line,
                steps=10,
            ).draw(turtle=turtle, colour="white", size=self.size + 2)  # type: ignore

        QuadraticBezierCurve.from_start_and_end(
            start=self.start,
            end=self.end,
            off_line=self.off_line,
            steps=10,
        ).draw(turtle=turtle, colour=original_colour, size=self.size)  # type: ignore


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

        QuadraticBezierCurve.from_start_and_end(
            start=self.start,
            end=self.end,
            off_line=self.off_line,
            steps=10,
        ).draw(turtle=turtle, colour="white", size=self.size + 2)

        QuadraticBezierCurve.from_start_and_end(
            start=self.end,
            end=self.start,
            off_line=self.off_line,
            steps=2,
        ).draw(turtle=turtle, colour="white", size=self.size + 2)
        turtle.pencolor(original_colour)

        curve = QuadraticBezierCurve.from_start_and_end(
            start=self.start,
            end=self.end,
            off_line=self.off_line,
            steps=10,
        )

        mouth_polygon = Polygon(vertices=curve.vertices)

        mouth_polygon.draw(
            turtle=turtle,
            fill=ColourFill(self.colour) if self.fill else None,
            colour=original_colour,
            size=self.size,
        )
