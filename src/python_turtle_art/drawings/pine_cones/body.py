from turtle import Turtle, Vec2D

from ...helpers.turtle import jump_to
from ...lines.offset_from_line import OffsetFromLine
from ...lines.quadratic_bezier_curve import QuadraticBezierCurve
from .face import CurvedMouth


class Limb(CurvedMouth):
    """Different name from CurvedMouth for readability."""

    pass


class Arm(Limb):
    def __init__(
        self,
        start: Vec2D,
        end: Vec2D,
        size: int,
        off_line: OffsetFromLine | None = None,
        outline: bool = True,
        n_wiggles: int = 1,
    ):
        self.start = start
        self.end = end
        self.off_line = OffsetFromLine() if off_line is None else off_line
        self.size = size
        self.outline = outline
        self.n_wiggles = n_wiggles

    def draw(self, turtle: Turtle):
        jump_to(turtle, self.start)

        wiggle_step_size = (1 / self.n_wiggles) * (self.end - self.start)

        multiplier = 1

        for n in range(self.n_wiggles):
            wiggle_offset = OffsetFromLine(
                proportion_lenth=self.off_line.proportion_lenth,
                offset=multiplier * self.off_line.offset,
            )

            QuadraticBezierCurve.from_start_and_end(
                start=self.start + n * wiggle_step_size,
                end=self.start + (n + 1) * wiggle_step_size,
                off_line=wiggle_offset,
                steps=10,
            ).draw(
                turtle=turtle,
                size=self.size,  # type: ignore
            )

            multiplier *= -1
