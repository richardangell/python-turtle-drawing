from turtle import Vec2D

import pytest

from python_turtle_art.vertices.vertices import ExtremeIndices, GetExtremeVerticesMixin


class DummyImplmentation(GetExtremeVerticesMixin):
    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices


def test_non_valid_axis_value_error():
    x = DummyImplmentation(vertices=(Vec2D(0, 0), Vec2D(10, 10)))

    with pytest.raises(ValueError, match="2 is not a valid Axis"):
        x.get_vertices_indices_with_min_and_max_values_on_axis(axis=2)


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
def test_get_vertices_indices_with_min_and_max_values_on_axis_y(
    coordinates, expected_min_index, expected_max_index
):
    expected = ExtremeIndices(minimum=expected_min_index, maximum=expected_max_index)

    x = DummyImplmentation(vertices=tuple(Vec2D(x, y) for x, y in coordinates))

    actual = x.get_vertices_indices_with_min_and_max_values_on_axis(axis=1)

    assert actual == expected


@pytest.mark.parametrize(
    ["coordinates", "expected_min_index", "expected_max_index"],
    [
        ([(0, 0), (10, 10), (0, 20), (-10, 10)], 3, 1),
        ([(-10, 10), (0, 0), (10, 10), (0, 20)], 0, 2),
        ([(0, 20), (-10, 10), (0, 0), (10, 10)], 1, 3),
        ([(10, 10), (0, 20), (-10, 10), (0, 0)], 2, 0),
        ([(0, 0), (10, 0), (10, 10), (0, 10)], 0, 1),
        ([(0, 0), (10, 0), (12, -3), (10, 10), (0, 10), (-3, 4)], 5, 2),
    ],
)
def test_get_vertices_indices_with_min_and_max_values_on_axis_x(
    coordinates, expected_min_index, expected_max_index
):
    expected = ExtremeIndices(minimum=expected_min_index, maximum=expected_max_index)

    x = DummyImplmentation(vertices=tuple(Vec2D(x, y) for x, y in coordinates))

    actual = x.get_vertices_indices_with_min_and_max_values_on_axis(axis=0)

    assert actual == expected
