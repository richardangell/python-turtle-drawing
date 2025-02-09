from __future__ import annotations

from math import sqrt
from turtle import Turtle, Vec2D
from typing import Optional, Union

from ..drawings.pine_cones.line import OffsetFromLine, get_points_on_curve
from ..fill import BaseFill
from ..helpers.turtle import jump_to
from .convex_polygon import ConvexPolygon


class ConvexKite(ConvexPolygon):
    """Class for drawing a convex kite shape.

    Args:
        vertices (tuple[Vec2D, ...]): Exactly 4 points of the kite.

    """

    def __init__(
        self,
        vertices: tuple[Vec2D, ...],
    ):
        """Define the convex kite by it's vertices."""
        self.vertices = vertices

        if len(vertices) != 4:
            raise ValueError("vertices must contain exactly 4 points.")

        self.corner_vertices_indices = (0, 1, 2, 3)

    @classmethod
    def from_origin_and_dimensions(
        cls,
        origin: Vec2D,
        height: int | float = sqrt(20),
        width: int | float = sqrt(20),
        diagonal_intersection_along_height: float = 0.5,
    ) -> ConvexKite:
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

    @staticmethod
    def calculate_kite_corner_vertices(
        origin: Vec2D,
        height: int | float = sqrt(20),
        width: int | float = sqrt(20),
        diagonal_intersection_along_height: float = 0.5,
    ) -> tuple[Vec2D, ...]:
        """Calculate the 4 corner certices from the supplied dimensions."""
        half_width = width / 2

        left_point = origin + Vec2D(
            x=-half_width, y=diagonal_intersection_along_height * height
        )
        right_point = origin + Vec2D(
            x=half_width, y=diagonal_intersection_along_height * height
        )
        top_point = origin + Vec2D(0, height)

        return (origin, left_point, top_point, right_point)

    def get_height(self) -> float:
        """Calculate the height of the kite."""
        bottom_vertex_index = self.corner_vertices_indices[0]
        top_vertex_index = self.corner_vertices_indices[2]

        delta = self.vertices[top_vertex_index] - self.vertices[bottom_vertex_index]

        return sqrt(delta * delta)

    def get_width(self) -> float:
        """Calculate the width of the kite."""
        left_vertex_index = self.corner_vertices_indices[1]
        right_vertex_index = self.corner_vertices_indices[3]

        delta = self.vertices[right_vertex_index] - self.vertices[left_vertex_index]

        return sqrt(delta * delta)


class CurvedConvexKite(ConvexKite):
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
    ) -> CurvedConvexKite:
        """Define a CurvedConvexKite from origin point and dimensions."""

        if len(off_lines) != 4:
            raise ValueError("off_lines must contain 4 elements.")

        kite_corner_points = ConvexKite.calculate_kite_corner_vertices(
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

        curved_convex_kite = CurvedConvexKite(
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


class CurvedConvexKiteFactory:
    """Factor that allows delaying the creation of CurvedConvexKite objects.

    Some arguments required in CurvedConvexKite.__init__ can be speficied in
    the initialisation of this class, the remaining arguments can be specified
    later when get_kite is called.

    """

    def __init__(
        self,
        origin: Optional[Vec2D] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        rotation: Optional[Union[int, float]] = None,
        rotation_point: Optional[Vec2D] = None,
        diagonal_intersection_along_height: Optional[float] = None,
    ):
        """Initialise the ConvexKite object."""
        self.origin = origin
        self.off_lines = off_lines
        self.height = height
        self.width = width
        self.rotation = rotation
        self.rotation_point = rotation_point
        self.diagonal_intersection_along_height = diagonal_intersection_along_height

    def get_kite(
        self,
        origin: Optional[Vec2D] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        rotation: Optional[Union[int, float]] = None,
        rotation_point: Optional[Vec2D] = None,
        diagonal_intersection_along_height: Optional[float] = None,
    ) -> CurvedConvexKite:
        """Return CurvedConvexKite object."""

        if origin is None:
            if self.origin is None:
                raise ValueError("origin not specified")
            else:
                origin = self.origin

        if off_lines is None:
            if self.off_lines is None:
                raise ValueError("off_lines not specified")
            else:
                off_lines = self.off_lines

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

        if rotation is None:
            if self.rotation is None:
                raise ValueError("rotation not specified")
            else:
                rotation = self.rotation

        if rotation_point is None and self.rotation_point is not None:
            rotation_point = self.rotation_point

        if diagonal_intersection_along_height is None:
            if self.diagonal_intersection_along_height is None:
                raise ValueError("diagonal_intersection_along_height not specified")
            else:
                diagonal_intersection_along_height = (
                    self.diagonal_intersection_along_height
                )

        return CurvedConvexKite.from_origin_and_dimensions(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=off_lines,
        )
