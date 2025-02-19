from turtle import Vec2D

import pytest

from python_turtle_art.vertices.vertices import ExtremeIndices, GetExtremeVerticesMixin


class DummyImplmentation(GetExtremeVerticesMixin):
    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices


@pytest.mark.parametrize(
    ["coordinates", "expected_min_index", "expected_max_index"],
    [
        ([(0, 0), (10, 10), (0, 20), (-10, 10)], 0, 2),
        ([(-10, 10), (0, 0), (10, 10), (0, 20)], 1, 3),
        ([(0, 20), (-10, 10), (0, 0), (10, 10)], 2, 0),
        ([(10, 10), (0, 20), (-10, 10), (0, 0)], 3, 1),
        ([(0, 0), (10, 0), (10, 10), (0, 10)], 0, 2),
        ([(0, 0), (10, 0), (12, -3), (10, 10), (0, 10), (-3, 4)], 2, 3),
    ],
)
def test_get_extreme_y_vertices_indices(
    coordinates, expected_min_index, expected_max_index
):
    expected = ExtremeIndices(minimum=expected_min_index, maximum=expected_max_index)

    x = DummyImplmentation(vertices=tuple(Vec2D(x, y) for x, y in coordinates))

    actual = x.get_extreme_y_vertices_indices()

    assert actual == expected
