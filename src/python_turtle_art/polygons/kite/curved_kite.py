from __future__ import annotations

from math import sqrt
from turtle import Turtle, Vec2D
from typing import Optional, Union

from ...fill import BaseFill
from ...helpers.turtle import jump_to
from ...line import OffsetFromLine, get_points_on_curve
from .kite import Kite


class CurvedKite(Kite):
    """Class for drawing a convex kite with curved edges."""

    def __init__(
        self,
        vertices: tuple[Vec2D, ...],
        corner_vertices_indices=tuple[int, ...],
    ):
        """Define the curved convex kite by it's vertices."""
        self.vertices = vertices

        if len(vertices) <= 4:
            raise ValueError("vertices must contain more than 4 points.")

        if len(corner_vertices_indices) != 4:
            raise ValueError("corner_vertices_indices must contain exactly 4 points.")

        self.corner_vertices_indices = corner_vertices_indices

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

        if len(off_lines) != 4:
            raise ValueError("off_lines must contain 4 elements.")

        kite_corner_points = Kite.calculate_kite_corner_vertices(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
        )
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

            curved_edges.extend(curve_points)

        curved_convex_kite = CurvedKite(
            vertices=tuple(curved_edges),
            corner_vertices_indices=tuple(
                x for x in range(0, len(curved_edges), steps_in_curves)
            ),
        )

        return curved_convex_kite

    def draw(
        self,
        turtle: Turtle,
        colour: str = "black",
        size: Optional[int] = None,
        fill: Optional[BaseFill] = None,
    ):
        """Jump to first vertex then draw the curved convex kite."""
        jump_to(turtle, self.vertices[0])
        super().draw(turtle=turtle, colour=colour, size=size, fill=fill)


class CurvedKiteFactory:
    """Factory that allows delaying the creation of CurvedKite objects.

    The arguments of CurvedKite.from_origin_and_dimensions can be speficied either in
    the initialisation of this class or later when the get_kite method is called.

    The rotation and rotation_point arguments are not used directly by this class.

    """

    def __init__(
        self,
        origin: Optional[Vec2D] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        diagonal_intersection_along_height: Optional[float] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
        # TODO: consider if rotation arguments could be moved somewhere else
        rotation: Optional[Union[int, float]] = None,
        rotation_point: Optional[Vec2D] = None,
    ):
        """Initialise the ConvexKite object."""
        self.origin = origin
        self.height = height
        self.width = width
        self.diagonal_intersection_along_height = diagonal_intersection_along_height
        self.off_lines = off_lines
        self.rotation = rotation
        self.rotation_point = rotation_point

    def get_kite(
        self,
        origin: Optional[Vec2D] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        diagonal_intersection_along_height: Optional[float] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
    ) -> CurvedKite:
        """Return CurvedKite object.

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
        )
