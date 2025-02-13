import pytest

from python_turtle_art.polygons.kites.curved_kite import CurvedKite
from python_turtle_art.polygons.kites.kite import Kite

from ....helpers import coords_iterable_to_vertices


def test_is_subclasses_kite():
    assert issubclass(CurvedKite, Kite)


def test_curved_kite_must_have_more_than_four_vertices():
    coords = [(0, 0), (7.5, 2.5), (5, 5), (7.5, 7.5)]

    vertices = coords_iterable_to_vertices(coords)

    with pytest.raises(ValueError, match="vertices must contain more than 4 points."):
        CurvedKite(vertices=vertices, corner_vertices_indices=(0, 1, 2, 3))
