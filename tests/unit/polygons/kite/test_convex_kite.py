from turtle import Vec2D

import pytest

from python_turtle_art.polygons.kite.convex_kite import ConvexKite


def test_cannot_initialise_non_convex_kite():
    coordinates = [[0, -3], [4, 8], [0, 7], [-4, 8]]

    vertices = tuple(Vec2D(coords[0], coords[1]) for coords in coordinates)

    with pytest.raises(
        ValueError, match="Polygon defined by supplied vertices are not convex."
    ):
        ConvexKite(vertices=vertices)
