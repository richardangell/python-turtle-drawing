from turtle import Vec2D

import pytest

from python_turtle_art.polygons.kite.kite import Kite
from python_turtle_art.polygons.polygon import Polygon


def test_is_polygon_subclass():
    assert issubclass(Kite, Polygon)


@pytest.mark.parametrize(
    "vertices",
    [
        (Vec2D(0, 0), Vec2D(0, 2), Vec2D(1, 0)),
        (Vec2D(0, 0), Vec2D(0, 2)),
        (Vec2D(0, 0),),
        (Vec2D(0, 0), Vec2D(0, 2), Vec2D(1, 0), Vec2D(1, 3), Vec2D(1, 4)),
    ],
)
def test_kite_requires_four_vertices(vertices):
    with pytest.raises(ValueError, match="vertices must contain exactly 4 points."):
        Kite(vertices=vertices)


def test_corner_vertices_indices():
    kite = Kite(vertices=(Vec2D(0, 0), Vec2D(1, 1), Vec2D(0, 2), Vec2D(-1, 1)))

    assert kite.corner_vertices_indices == (0, 1, 2, 3)


def test_calculate_kite_corner_vertices():
    pass
