from __future__ import annotations

from math import sqrt
from turtle import Vec2D

from ..polygon import Polygon


class Kite(Polygon):
    """Class for drawing a kite shape.

    Args:
        vertices (tuple[Vec2D, ...]): Exactly 4 points of the kite.

    """

    def __init__(
        self,
        vertices: tuple[Vec2D, ...],
    ):
        """Define the kite by it's vertices."""
        self.vertices = vertices
        self.corner_vertices_indices = (0, 1, 2, 3)

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Set vertices attribute and check there are exactly 4 points."""
        if len(vertices) != 4:
            raise ValueError("vertices must contain exactly 4 points.")
        self._vertices = vertices

    @property
    def corner_vertices_indices(self) -> tuple[int, ...]:
        return self._corner_vertices_indices

    @corner_vertices_indices.setter
    def corner_vertices_indices(self, corner_vertices_indices: tuple[int, ...]) -> None:
        """Set corner_vertices_indices attribute and check there are 4 provided."""
        if len(corner_vertices_indices) != 4:
            raise ValueError("corner_vertices_indices must contain exactly 4 points.")
        self._corner_vertices_indices = corner_vertices_indices

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

        return Kite(vertices=vertices)

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
