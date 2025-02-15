from turtle import Vec2D

import pytest

from python_turtle_art.lines.offset_from_line import OffsetFromLine
from python_turtle_art.polygons.kites.convex_curved_kite import (
    ConvexCurvedKite,
)
from python_turtle_art.polygons.kites.curved_kite import CurvedKite

from ....helpers import coords_iterable_to_vertices


def test_is_subclasses_curved_kite():
    assert issubclass(ConvexCurvedKite, CurvedKite)


def test_cannot_initialise_non_convex_curved_kite():
    coords = [(0, 0), (7.5, 2.5), (5, 5), (7.5, 7.5), (0, 10), (-5, 5)]

    vertices = coords_iterable_to_vertices(coords)

    with pytest.raises(
        ValueError, match="Polygon defined by supplied vertices are not convex."
    ):
        ConvexCurvedKite(
            vertices=vertices,
            corner_vertices_indices=(0, 2, 4, 5),
        )


def test_cannot_initialise_non_convex_curved_kite_from_dimensions():
    with pytest.raises(
        ValueError, match="Polygon defined by supplied vertices are not convex."
    ):
        ConvexCurvedKite.from_origin_and_dimensions(
            origin=Vec2D(0, 0),
            height=50,
            width=25,
            diagonal_intersection_along_height=0.5,
            off_lines=(
                OffsetFromLine(0.5, 20),
                OffsetFromLine(0.5, 20),
                OffsetFromLine(0.5, 1),
                OffsetFromLine(0.5, 1),
            ),
        )
