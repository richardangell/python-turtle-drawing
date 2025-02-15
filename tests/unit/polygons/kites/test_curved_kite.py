from math import sqrt
from operator import gt, lt
from turtle import Vec2D

import pytest

from python_turtle_art.lines.offset_from_line import OffsetFromLine
from python_turtle_art.polygons.kites.curved_kite import CurvedKite
from python_turtle_art.polygons.kites.kite import Kite

from ....helpers import coords_iterable_to_vertices
from .test_kite import KITE_DIMENSIONS_PARAMS


def test_is_subclasses_kite():
    assert issubclass(CurvedKite, Kite)


def test_curved_kite_must_have_more_than_four_vertices():
    coords = [(0, 0), (7.5, 2.5), (5, 5), (7.5, 7.5)]

    vertices = coords_iterable_to_vertices(coords)

    with pytest.raises(ValueError, match="vertices must contain more than 4 points."):
        CurvedKite(vertices=vertices, corner_vertices_indices=(0, 1, 2, 3))


def test_cannot_initialise_with_two_points_in_curves():
    with pytest.raises(ValueError, match="vertices must contain more than 4 points."):
        CurvedKite.from_origin_and_dimensions(
            origin=Vec2D(0, 0),
            height=10,
            width=10,
            diagonal_intersection_along_height=0.4,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=2,
        )


def test_can_initialise_non_convex_curved_kite():
    coords = [(0, 0), (7.5, 2.5), (5, 5), (7.5, 7.5), (0, 10), (-5, 5)]

    vertices = coords_iterable_to_vertices(coords)

    kite = CurvedKite(
        vertices=vertices,
        corner_vertices_indices=(0, 2, 4, 5),
    )

    assert not kite.is_convex()


@pytest.mark.parametrize(
    ["offset", "expected_convexity"],
    [
        (0.1, True),
        (1, True),
        (2, True),
        (3, True),
        (3.5, True),
        (3.6, True),
        (3.7, True),
        (3.8, False),
        (4, False),
        (10, False),
    ],
)
def test_increasing_curve_offset_distance_produces_non_convex_kite(
    offset, expected_convexity
):
    offsets = [offset] * 4

    offsets_from_line = tuple(OffsetFromLine(offset=offset) for offset in offsets)

    kite = CurvedKite.from_origin_and_dimensions(
        origin=Vec2D(0, -5),
        height=10,
        width=10,
        diagonal_intersection_along_height=0.5,
        off_lines=offsets_from_line,
        steps_in_curves=20,
    )

    assert kite.is_convex() is expected_convexity


@pytest.mark.parametrize("offset", [-0.1, -0.3, -0.5, -1, -2, -5, -10, -20])
def test_any_inwards_curvature_produces_non_convex_kite(offset):
    # really large values should lead to the kite being self-intersecting
    offsets = [offset] * 4

    offsets_from_line = tuple(OffsetFromLine(offset=offset) for offset in offsets)

    kite = CurvedKite.from_origin_and_dimensions(
        origin=Vec2D(0, -5),
        height=10,
        width=10,
        diagonal_intersection_along_height=0.5,
        off_lines=offsets_from_line,
        steps_in_curves=20,
    )

    assert not kite.is_convex()


@pytest.mark.parametrize(
    "curved_kite_function_to_call",
    [CurvedKite.from_origin_and_dimensions, CurvedKite.get_curved_kite_vertices],
)
class TestVerticesDefiningCurvedKite:
    """Tests for the vertices of CurvedKite objects.

    CurvedKite objects in this test are produced by both the from_origin_and_dimensions
    and get_curved_kite_vertices methods.

    """

    def test_error_if_off_lines_not_four_elements(self, curved_kite_function_to_call):
        with pytest.raises(ValueError, match="off_lines must contain 4 elements."):
            curved_kite_function_to_call(
                origin=Vec2D(0, 0),
                height=10,
                width=10,
                diagonal_intersection_along_height=0.4,
                off_lines=(OffsetFromLine(), OffsetFromLine(), OffsetFromLine()),
                steps_in_curves=5,
            )

    def test_vertices_are_unique(self, curved_kite_function_to_call):
        output = curved_kite_function_to_call(
            origin=Vec2D(0, 0),
            height=10,
            width=10,
            diagonal_intersection_along_height=0.4,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=5,
        )

        if isinstance(output, CurvedKite):
            actual_vertices = output.vertices
        else:
            actual_vertices = output[0]

        assert len(set(actual_vertices)) == len(actual_vertices)

    @pytest.mark.parametrize("steps_in_curves", [3, 6, 12])
    def test_expected_number_of_vertices_given_curve_steps(
        self, curved_kite_function_to_call, steps_in_curves
    ):
        output = curved_kite_function_to_call(
            origin=Vec2D(0, 0),
            height=10,
            width=10,
            diagonal_intersection_along_height=0.4,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=steps_in_curves,
        )

        if isinstance(output, CurvedKite):
            actual_vertices = output.vertices
        else:
            actual_vertices = output[0]

        assert len(actual_vertices) == (steps_in_curves - 1) * 4

    @pytest.mark.parametrize("steps_in_curves", [3, 5, 10])
    def test_corner_indices_given_curve_steps(
        self, curved_kite_function_to_call, steps_in_curves
    ):
        output = curved_kite_function_to_call(
            origin=Vec2D(0, 0),
            height=10,
            width=10,
            diagonal_intersection_along_height=0.4,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=steps_in_curves,
        )

        if isinstance(output, CurvedKite):
            actual_corner_indices = output.corner_vertices_indices
        else:
            actual_corner_indices = output[1]

        expected_corner_indices = (
            0,
            1 * (steps_in_curves - 1),
            2 * (steps_in_curves - 1),
            3 * (steps_in_curves - 1),
        )

        assert actual_corner_indices == expected_corner_indices

    @pytest.mark.parametrize(
        [
            "origin",
            "height",
            "width",
            "diagonal_intersection_along_height",
            "expected_coordinates",
        ],
        KITE_DIMENSIONS_PARAMS,
    )
    def test_corner_indices_correct(
        self,
        curved_kite_function_to_call,
        origin,
        height,
        width,
        diagonal_intersection_along_height,
        expected_coordinates,
    ):
        output = curved_kite_function_to_call(
            origin=Vec2D(*origin),
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=3,
        )

        if isinstance(output, CurvedKite):
            actual_vertices = output.vertices
            actual_corner_indices = output.corner_vertices_indices
        else:
            actual_vertices = output[0]
            actual_corner_indices = output[1]

        for corner_index, expected_coords in zip(
            actual_corner_indices, expected_coordinates, strict=False
        ):
            assert actual_vertices[corner_index] == pytest.approx(
                Vec2D(*expected_coords)
            )

    @pytest.mark.parametrize(
        [
            "non_zero_offset_index",
            "outer_curve_vertex_x_coord_inequality",
            "outer_curve_vertex_y_coord_inequality",
        ],
        [
            (0, lt, lt),
            (1, lt, gt),
            (2, gt, gt),
            (3, gt, lt),
        ],
    )
    def test_offset_from_line_creates_curve_in_expected_direction(
        self,
        curved_kite_function_to_call,
        non_zero_offset_index,
        outer_curve_vertex_x_coord_inequality,
        outer_curve_vertex_y_coord_inequality,
    ):
        """Test that off_lines extrudes away from the kite in expected direction.

        This test uses steps_in_curves = 3 which means that each edge will have an
        additional vertex in the middle.

        Given the index of the OffsetFromLine object that has a non-zero value that is
        also large relative to the dimensions of the kite - we expect that the point
        which lies outside the kite edges will be furthest point from (0, 0) of all
        the vertices of the kite.

        """
        offsets = [0, 0, 0, 0]
        offsets[non_zero_offset_index] = 20

        expected_outer_curve_vertex_index = (2 * non_zero_offset_index) + 1

        offsets_from_line = tuple(OffsetFromLine(offset=offset) for offset in offsets)

        output = curved_kite_function_to_call(
            origin=Vec2D(0, -5),
            height=10,
            width=10,
            diagonal_intersection_along_height=0.5,
            off_lines=offsets_from_line,
            steps_in_curves=3,
        )

        if isinstance(output, CurvedKite):
            actual_vertices = output.vertices
            actual_corner_indices = output.corner_vertices_indices
        else:
            actual_vertices = output[0]
            actual_corner_indices = output[1]

        assert expected_outer_curve_vertex_index not in actual_corner_indices

        # this is the vertex that should be protruding out from the kite
        expected_outer_curve_vertex = actual_vertices[expected_outer_curve_vertex_index]

        prior_index = expected_outer_curve_vertex_index - 1
        next_index = (
            expected_outer_curve_vertex_index + 1
            if expected_outer_curve_vertex_index < 7
            else 0
        )

        sum_prior_and_next = actual_vertices[prior_index] + actual_vertices[next_index]

        assert expected_outer_curve_vertex != pytest.approx(
            Vec2D(sum_prior_and_next[0] / 2, sum_prior_and_next[1] / 2)
        )

        for vertex_index, vertex in enumerate(actual_vertices):
            if vertex_index != expected_outer_curve_vertex_index:
                assert outer_curve_vertex_x_coord_inequality(
                    expected_outer_curve_vertex[0], vertex[0]
                )
                assert outer_curve_vertex_y_coord_inequality(
                    expected_outer_curve_vertex[1], vertex[1]
                )

    def test_zero_offset_from_line_creates_straight_lined_kite(
        self, curved_kite_function_to_call
    ):
        offsets = [0, 0, 0, 0]

        offsets_from_line = tuple(OffsetFromLine(offset=offset) for offset in offsets)

        output = curved_kite_function_to_call(
            origin=Vec2D(0, -5),
            height=10,
            width=10,
            diagonal_intersection_along_height=0.5,
            off_lines=offsets_from_line,
            steps_in_curves=3,
        )

        if isinstance(output, CurvedKite):
            actual_vertices = output.vertices
            actual_corner_indices = output.corner_vertices_indices
        else:
            actual_vertices = output[0]
            actual_corner_indices = output[1]

        for vertex_index in (1, 3, 5, 7):
            assert vertex_index not in actual_corner_indices

            prior_index = vertex_index - 1
            next_index = vertex_index + 1 if vertex_index < 7 else 0

            sum_prior_and_next = (
                actual_vertices[prior_index] + actual_vertices[next_index]
            )

            assert actual_vertices[vertex_index] == pytest.approx(
                Vec2D(sum_prior_and_next[0] / 2, sum_prior_and_next[1] / 2)
            )


class TestGetHeight:
    """Tests for the CurvedKite.get_height method."""

    @pytest.mark.parametrize(
        ["coordinates", "corner_indices", "expected"],
        [
            (((0, 0), (-5, 5), (0, 10), (2.5, 7.5), (5, 5)), (0, 1, 2, 4), 10),
            (((-2, -2), (-4, 0), (-3, 4), (-2, 9), (3, 3)), (0, 1, 3, 4), 11),
            (((0, 0), (-2, 3), (-5, 5), (1, 10), (5, 5)), (0, 2, 3, 4), sqrt(101)),
        ],
    )
    def test_expected_height(self, coordinates, corner_indices, expected):
        vertices = coords_iterable_to_vertices(coordinates)

        kite = CurvedKite(vertices=vertices, corner_vertices_indices=corner_indices)

        assert kite.get_height() == expected

    @pytest.mark.parametrize("diagonal_intersection_along_height", [-0.9, 0.9, 2.2])
    @pytest.mark.parametrize("height", [9, 3.1])
    def test_height_matches_height_from_initialisation(
        self, height, diagonal_intersection_along_height
    ):
        kite = CurvedKite.from_origin_and_dimensions(
            origin=Vec2D(3, 4),
            height=height,
            width=5,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=5,
        )

        assert kite.get_height() == pytest.approx(height)

    @pytest.mark.parametrize("about_point", [Vec2D(-3, -4), Vec2D(0, 0)])
    @pytest.mark.parametrize("angle", [13, 345])
    def test_height_unchanged_under_rotation(self, angle, about_point):
        height = 8

        kite = CurvedKite.from_origin_and_dimensions(
            origin=Vec2D(4, 5),
            height=height,
            width=5,
            diagonal_intersection_along_height=0.5,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=5,
        ).rotate(angle=angle, about_point=about_point)

        assert kite.get_height() == pytest.approx(height)


class TestGetWidth:
    """Tests for the CurvedKite.get_width method."""

    @pytest.mark.parametrize(
        ["coordinates", "corner_indices", "expected"],
        [
            (
                ((0, 0), (-3, -3), (-5, 5), (-3, 7), (0, 10), (3, 7), (5, 5), (3, 4)),
                (0, 2, 4, 6),
                10,
            ),
            (
                ((-2, -2), (-4, 0), (-2, 9), (0, 7), (2, 4), (3, 3)),
                (0, 1, 2, 5),
                sqrt(49 + 9),
            ),
        ],
    )
    def test_expected_width(self, coordinates, corner_indices, expected):
        vertices = coords_iterable_to_vertices(coordinates)

        kite = CurvedKite(
            vertices=vertices,
            corner_vertices_indices=corner_indices,
        )

        assert kite.get_width() == expected

    @pytest.mark.parametrize("diagonal_intersection_along_height", [-0.2, 0.7, 1.1])
    @pytest.mark.parametrize("width", [10, 5.5])
    def test_width_matches_height_from_initialisation(
        self, width, diagonal_intersection_along_height
    ):
        kite = CurvedKite.from_origin_and_dimensions(
            origin=Vec2D(2, 5),
            height=3,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=5,
        )

        assert kite.get_width() == width

    @pytest.mark.parametrize("about_point", [Vec2D(0, 0), Vec2D(-1, -3)])
    @pytest.mark.parametrize("angle", [90, 130])
    def test_width_unchanged_under_rotation(self, angle, about_point):
        width = 5

        kite = CurvedKite.from_origin_and_dimensions(
            origin=Vec2D(-1, -5),
            height=10,
            width=width,
            diagonal_intersection_along_height=0.5,
            off_lines=(
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
                OffsetFromLine(),
            ),
            steps_in_curves=5,
        ).rotate(angle=angle, about_point=about_point)

        assert kite.get_width() == pytest.approx(width)
