from __future__ import annotations

from turtle import Vec2D

from ...line import OffsetFromLine, get_points_on_curve
from .kite import Kite


class CurvedKite(Kite):
    """Class for drawing a convex kite with curved edges."""

    def __init__(
        self,
        vertices: tuple[Vec2D, ...],
        corner_vertices_indices: tuple[int, ...],
    ):
        """Define the curved convex kite by it's vertices."""
        self.vertices = vertices
        self.corner_vertices_indices = corner_vertices_indices

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Set vertices attribute and check there are at least 3 points."""
        if len(vertices) <= 4:
            raise ValueError("vertices must contain more than 4 points.")
        self._vertices = vertices

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
    ) -> CurvedKite:
        """Define a CurvedKite from origin point and dimensions."""

        vertices, corner_vertices_indices = CurvedKite.get_curved_kite_vertices(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=off_lines,
            steps_in_curves=steps_in_curves,
        )

        return CurvedKite(
            vertices=vertices, corner_vertices_indices=corner_vertices_indices
        )

    @staticmethod
    def get_curved_kite_vertices(
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
    ) -> tuple[tuple[Vec2D, ...], tuple[int, ...]]:
        if len(off_lines) != 4:
            raise ValueError("off_lines must contain 4 elements.")

        kite_corner_points = Kite.calculate_kite_corner_vertices(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
        )

        curved_edges: list[Vec2D]
        curved_edges = []

        for index in range(len(kite_corner_points)):
            end_index = index + 1
            if end_index == 4:
                end_index = 0

            control_point = off_lines[index].to_point(
                kite_corner_points[index], kite_corner_points[end_index]
            )

            curve_points = get_points_on_curve(
                start=kite_corner_points[index],
                end=kite_corner_points[end_index],
                off_line_point=control_point,
                steps=steps_in_curves,
            )

            curved_edges.extend(curve_points[:-1])

        vertices = tuple(curved_edges)

        corner_vertices_indices = tuple(
            x for x in range(0, len(curved_edges), steps_in_curves - 1)
        )

        return vertices, corner_vertices_indices
