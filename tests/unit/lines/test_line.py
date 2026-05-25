from turtle import Vec2D

import pytest

from python_turtle_art.lines.line import ExtremeIndices, Line


def test_jump_to_vertex_index():
    assert Line._jump_to_vertex_index == 0


def test_cannot_initiate_line_with_less_than_two_vertices():
    with pytest.raises(ValueError, match="vertices must contain at least 2 points."):
        Line(vertices=(Vec2D(0, 1),))


class TestGetVerticesIndicesWithMinAndMaxValuesOnAxis:
    def test_non_valid_axis_value_error(self):
        x = Line(vertices=(Vec2D(0, 0), Vec2D(10, 10)))

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
        self, coordinates, expected_min_index, expected_max_index
    ):
        expected = ExtremeIndices(
            minimum=expected_min_index, maximum=expected_max_index
        )

        x = Line(vertices=tuple(Vec2D(x, y) for x, y in coordinates))

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
        self, coordinates, expected_min_index, expected_max_index
    ):
        expected = ExtremeIndices(
            minimum=expected_min_index, maximum=expected_max_index
        )

        x = Line(vertices=tuple(Vec2D(x, y) for x, y in coordinates))

        actual = x.get_vertices_indices_with_min_and_max_values_on_axis(axis=0)

        assert actual == expected
