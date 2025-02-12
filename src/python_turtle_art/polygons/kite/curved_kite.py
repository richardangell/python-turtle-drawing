from __future__ import annotations

from math import sqrt
from turtle import Vec2D
from typing import Optional, Union

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
        height: int | float = sqrt(20),
        width: int | float = sqrt(20),
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
        height: int | float = sqrt(20),
        width: int | float = sqrt(20),
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


class CurvedKiteFactory:
    """Factory allowing delay of CurvedKite creation with from_origin_and_dimensions.

    The arguments of CurvedKite.from_origin_and_dimensions can be speficied either in
    the initialisation of this class or later when the get_kite method is called.

    The rotation argument must be specified. When the CurvedKite object is created with
    get_kite it will be rotated by rotation degrees about the origin point.

    """

    def __init__(
        self,
        rotation: Union[int, float],
        origin: Optional[Vec2D] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        diagonal_intersection_along_height: Optional[float] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
    ):
        """Initialise the CurvedKiteFactory with optional args for CurvedKite."""
        self.rotation = rotation
        self.origin = origin
        self.height = height
        self.width = width
        self.diagonal_intersection_along_height = diagonal_intersection_along_height
        self.off_lines = off_lines

    def get_kite(
        self,
        origin: Optional[Vec2D] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        diagonal_intersection_along_height: Optional[float] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
    ) -> CurvedKite:
        """Return CurvedKite object and rotate about origin.

        If any of the arguments were not specified during initialisation of the
        CurvedKiteFactory object, they can be specified when get_kite is called. If
        however an argument is not specified during initialisation and also not
        specified when get_kite is called an exception will be raised.

        """

        if origin is None:
            if self.origin is None:
                raise ValueError("origin not specified")
            else:
                origin = self.origin

        if height is None:
            if self.height is None:
                raise ValueError("height not specified")
            else:
                height = self.height

        if width is None:
            if self.width is None:
                raise ValueError("width not specified")
            else:
                width = self.width

        if diagonal_intersection_along_height is None:
            if self.diagonal_intersection_along_height is None:
                raise ValueError("diagonal_intersection_along_height not specified")
            else:
                diagonal_intersection_along_height = (
                    self.diagonal_intersection_along_height
                )

        if off_lines is None:
            if self.off_lines is None:
                raise ValueError("off_lines not specified")
            else:
                off_lines = self.off_lines

        return CurvedKite.from_origin_and_dimensions(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=off_lines,
        ).rotate(angle=self.rotation, about_point=origin)
