from turtle import Vec2D

import pytest

from python_turtle_art.line import OffsetFromLine
from python_turtle_art.polygons.kite.convex_curved_kite import (
    ConvexCurvedKite,
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
