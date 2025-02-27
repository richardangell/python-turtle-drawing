from turtle import Vec2D

import pytest

from python_turtle_art.polygons.kites.convex_kite import ConvexKite
from python_turtle_art.polygons.kites.kite import Kite

from ....helpers import coords_iterable_to_vertices


def test_is_subclasses_curved_kite():
    assert issubclass(ConvexKite, Kite)


def test_cannot_initialise_non_convex_kite():
    coordinates = [(0, -3), (4, 8), (0, 7), (-4, 8)]

    vertices = coords_iterable_to_vertices(coordinates)

    with pytest.raises(
        ValueError, match="Polygon defined by supplied vertices are not convex."
    ):
        ConvexKite(vertices=vertices)


def test_cannot_initialise_non_convex_kite_from_dimensions():
    """diagonal_intersection_along_height > 1 create arrow head shape."""
    with pytest.raises(
        ValueError, match="Polygon defined by supplied vertices are not convex."
    ):
        ConvexKite.from_origin_and_dimensions(
            origin=Vec2D(0, 0),
            height=50,
            width=25,
            diagonal_intersection_along_height=1.1,
        )
