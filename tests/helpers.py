from turtle import Vec2D
from typing import Iterable


def coords_iterable_to_vertices(
    coordinates: Iterable[tuple[int, int]],
) -> tuple[Vec2D, ...]:
    """Convert coordinates supplied in tuples to Vec2D objects."""
    return tuple(Vec2D(*coords) for coords in coordinates)
