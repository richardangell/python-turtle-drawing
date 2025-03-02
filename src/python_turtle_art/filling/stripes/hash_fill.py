from turtle import RawTurtle

from ...polygons.convex_polygon import BaseConvexFill, ConvexPolygon
from .stripes_calculation import get_filling_lines


class HashFill(BaseConvexFill):
    """Fill a convex polygon with crossed horizontal and vertical stripes.

    Args:
        gap (int): distance between each stripe.
        origin (int): the origin for horizontal stripes (y-coordinate) and
            vertical stripes (x-coordinate) that they will be drawn relative to.
        size (int): pen size for the stripes.
        colour (str): pen colour for the stripes.

    """

    def __init__(self, gap: int, origin: int = 0, size: int = 1, colour: str = "black"):
        self.gap = gap
        self.origin = origin
        self.size = size
        self.colour = colour

    def fill(self, turtle: RawTurtle, polygon: ConvexPolygon):
        """Fill a convex polygon with crossed horizontal and vertical stripes.

        Args:
            turtle (Turtle): turtle graphics object.
            polygon (ConvexPolygon): convex polygon to fill.

        """
        vertical_stripes = get_filling_lines(
            origin=self.origin, gap=self.gap, polygon=polygon, axis=0
        )
        horizontal_stripes = get_filling_lines(
            origin=self.origin, gap=self.gap, polygon=polygon, axis=1
        )

        for stripe in vertical_stripes:
            stripe.draw(turtle=turtle, colour=self.colour, size=self.size)

        for stripe in horizontal_stripes:
            stripe.draw(turtle=turtle, colour=self.colour, size=self.size)
