from math import sqrt

import pytest

from python_turtle_art.polygons.polygon import Polygon

from ...helpers import coords_iterable_to_vertices


class TestIsConvex:
    """Tests for the Polygon.is_convex method."""

    @pytest.mark.parametrize(
        "vertices_manipulation",
        [
            pytest.param(lambda x: x, id="no maniupulation"),
            pytest.param(reversed, id="reverse"),
            pytest.param(lambda x: x[1:] + [x[0]], id="move first to end"),
            pytest.param(lambda x: [[c[0], -c[1]] for c in x], id="vertical flip"),
            pytest.param(lambda x: [[-c[0], c[1]] for c in x], id="horizontal flip"),
        ],
    )
    @pytest.mark.parametrize(
        "coordinates",
        [
            pytest.param([[0, 0], [0, 1], [1, 0]], id="right angle triangle"),
            pytest.param([[0, 0], [2, 0], [1, 2]], id="isosceles triagnle"),
            pytest.param([[-1, -1], [0, 5], [3, -0.5]], id="scalene triangle"),
            pytest.param([[0, 0], [1, 0], [1, 1], [0, 1]], id="square"),
            pytest.param([[-5, -5], [-3, -5], [-3, -2], [-5, -2]], id="rectangle"),
            pytest.param([[-3, -3], [3, -3], [4, 0], [-2, 0]], id="parallelogram"),
            pytest.param(
                [[-4, 0], [0, 0], [sqrt(8), sqrt(8)], [sqrt(8) - 4, sqrt(8)]],
                id="rhombus",
            ),
            pytest.param([[0, -3], [4, 8], [0, 9], [-4, 8]], id="kite"),
            pytest.param([[0, 0], [5, 0], [4, 3], [1, 3]], id="isosceles trapezoid"),
            pytest.param(
                [[-3, -2], [-4, 7], [3, 6], [2, -5]], id="irregular quadrilateral"
            ),
            pytest.param([[0, 0], [2, 0], [3, 3], [1, 5], [-2, 3]], id="pentagon"),
        ],
    )
    def test_convex_polygon(self, coordinates, vertices_manipulation):
        """Test convex polygons correctly identified."""

        vertices = coords_iterable_to_vertices(vertices_manipulation(coordinates))

        polygon = Polygon(vertices=vertices)

        assert polygon.is_convex()

    @pytest.mark.parametrize(
        "coordinates",
        [
            pytest.param([[0, 0], [0, 1], [1, 0]], id="right angle triangle"),
            pytest.param([[0, 0], [2, 0], [1, 2]], id="isosceles triagnle"),
            pytest.param([[-1, -1], [0, 5], [3, -0.5]], id="scalene triangle"),
            pytest.param([[0, 0], [1, 0], [1, 1], [0, 1]], id="square"),
            pytest.param([[-5, -5], [-3, -5], [-3, -2], [-5, -2]], id="rectangle"),
            pytest.param([[-3, -3], [3, -3], [4, 0], [-2, 0]], id="parallelogram"),
            pytest.param(
                [[-4, 0], [0, 0], [sqrt(8), sqrt(8)], [sqrt(8) - 4, sqrt(8)]],
                id="rhombus",
            ),
            pytest.param([[0, -3], [4, 8], [0, 9], [-4, 8]], id="kite"),
            pytest.param([[0, 0], [5, 0], [4, 3], [1, 3]], id="isosceles trapezoid"),
            pytest.param(
                [[-3, -2], [-4, 7], [3, 6], [2, -5]], id="irregular quadrilateral"
            ),
            pytest.param([[0, 0], [2, 0], [3, 3], [1, 5], [-2, 3]], id="pentagon"),
        ],
    )
    def test_self_intersecting_polygon_non_convex(self, coordinates):
        """Test self-intersecting polygons are identified as non-convex.

        Note, the first 3 cases are triangles so are not self-intersecting when the
        3rd point is moved to the 2nd position.

        """

        out_of_order_coordinates = [
            coordinates[0],
            coordinates[2],
            coordinates[1],
        ] + coordinates[3:]

        vertices = coords_iterable_to_vertices(out_of_order_coordinates)

        polygon = Polygon(vertices=vertices)

        if len(coordinates) == 3:
            assert polygon.is_convex()

        else:
            assert not polygon.is_convex()

    @pytest.mark.parametrize(
        "vertices_manipulation",
        [
            pytest.param(lambda x: x, id="no maniupulation"),
            pytest.param(reversed, id="reverse"),
            pytest.param(lambda x: x[1:] + [x[0]], id="move first to end"),
            pytest.param(lambda x: [[c[0], -c[1]] for c in x], id="vertical flip"),
            pytest.param(lambda x: [[-c[0], c[1]] for c in x], id="horizontal flip"),
        ],
    )
    @pytest.mark.parametrize(
        "coordinates",
        [
            pytest.param(
                [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]],
                id="square, top edge in centre",
            ),
            pytest.param(
                [
                    [0, 5],
                    [1, 10],
                    [2, 5],
                    [10, 5],
                    [3, 2],
                    [6, -10],
                    [1, 0],
                    [-5, -10],
                    [-2, 2],
                    [-9, 5],
                ],
                id="star",
            ),
        ],
    )
    def test_non_convex_polygon(self, coordinates, vertices_manipulation):
        """Test non convex polygons are correctly identified."""

        vertices = coords_iterable_to_vertices(vertices_manipulation(coordinates))

        polygon = Polygon(vertices=vertices)

        assert not polygon.is_convex()
