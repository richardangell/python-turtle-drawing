from turtle import Turtle
from typing import Optional

from ..fill import BaseFill
from .polygon import Polygon


class ConvexPolygon(Polygon):
    """Class for drawing a convex polygon."""

    def draw(
        self,
        turtle: Turtle,
        colour: str = "black",
        size: Optional[int] = None,
        fill: Optional[BaseFill] = None,
    ):
        """Draw polygon with optional filling."""

        if fill is not None:
            fill.pre_draw(turtle)

        super().draw(turtle=turtle, colour=colour, size=size)

        if fill is not None:
            fill.post_draw(turtle)
