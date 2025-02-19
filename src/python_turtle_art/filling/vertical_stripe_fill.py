from turtle import Turtle

from ..polygons.convex_polygon import BaseConvexFill, ConvexPolygon
from .stripes import get_filling_lines


class VerticalStripeFill(BaseConvexFill):
    """Fill a convex polygon with vertical stripes.

    Args:
        gap (int): distance between each stripe.
        origin (int): x-coordinate of the origin vertical stripes will be drawn
            relative to.

    """

    axis: int = 0

    def __init__(self, gap: int, size: int = 1, colour: str = "black", origin: int = 0):
        self.gap = gap
        self.size = size
        self.colour = colour
        self.origin = origin

    def fill(self, turtle: Turtle, polygon: ConvexPolygon):
        """Fill a convex polygon with horizontal stipes.

        Args:
            turtle (Turtle): turtle graphics object.
            polygon (ConvexPolygon): convex polygon to fill.

        """
        stripes = get_filling_lines(
            origin=self.origin, gap=self.gap, polygon=polygon, axis=self.axis
        )

        for stripe in stripes:
            stripe.draw(turtle=turtle, size=self.size, colour=self.colour)
