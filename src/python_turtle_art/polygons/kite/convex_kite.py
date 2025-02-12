from math import sqrt
from turtle import Vec2D

from ..convex_polygon import ConvexPolygon
from .kite import Kite


class ConvexKite(ConvexPolygon, Kite):
    """Class representing a convex kite shape."""

    @classmethod
    def from_origin_and_dimensions(
        cls,
        origin: Vec2D,
        height: int | float = sqrt(20),
        width: int | float = sqrt(20),
        diagonal_intersection_along_height: float = 0.5,
    ) -> Kite:
        """Define a convex kite from origin point and dimensions.

        Args:
            origin (Vec2D): bottom point of the kite.
            height (Union[int, float]): height of the kite.
            width (Union[int, float]): width of the kite.
            diagonal_intersection_along_height (float): proportion of the distance
                along the vertical bisector that the vertical bisector intersects
                with the horizontal bisector.

        """
        vertices = cls.calculate_kite_corner_vertices(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
        )

        return ConvexKite(vertices=vertices)
