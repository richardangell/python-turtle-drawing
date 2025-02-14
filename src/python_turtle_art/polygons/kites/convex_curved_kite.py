from __future__ import annotations

from turtle import Vec2D

from ...lines.offset_from_line import OffsetFromLine
from ..convex_mixin import ConvexMixin
from .curved_kite import CurvedKite


class ConvexCurvedKite(ConvexMixin, CurvedKite):
    """Class representing a convex kite shape."""

    @classmethod
    def from_origin_and_dimensions(
        cls,
        origin: Vec2D,
        height: int | float = 20,
        width: int | float = 20,
        diagonal_intersection_along_height: float = 0.5,
        off_lines: tuple[OffsetFromLine, ...] = (
            OffsetFromLine(),
            OffsetFromLine(),
            OffsetFromLine(),
            OffsetFromLine(),
        ),
        steps_in_curves: int = 20,
    ) -> ConvexCurvedKite:
        """Define a convex kite from origin point and dimensions.

        Args:
            origin (Vec2D): bottom point of the kite.
            height (Union[int, float]): height of the kite.
            width (Union[int, float]): width of the kite.
            diagonal_intersection_along_height (float): proportion of the distance
                along the vertical bisector that the vertical bisector intersects
                with the horizontal bisector.

        """
        vertices, corner_vertices_indices = CurvedKite.get_curved_kite_vertices(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=off_lines,
            steps_in_curves=steps_in_curves,
        )

        return ConvexCurvedKite(
            vertices=vertices,
            corner_vertices_indices=corner_vertices_indices,
        )
