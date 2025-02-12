from math import sqrt
from turtle import Vec2D

import pytest

from python_turtle_art.polygons.kite.kite import Kite
from python_turtle_art.polygons.polygon import Polygon

from ....helpers import coords_iterable_to_vertices

KITE_DIMENSIONS_PARAMS = [
    ((0, 0), 10, 10, 0.5, [(0, 0), (-5, 5), (0, 10), (5, 5)]),
    ((0, 0), 5, 10, 0.5, [(0, 0), (-5, 2.5), (0, 5), (5, 2.5)]),
    ((0, 0), 10, 5, 0.5, [(0, 0), (-2.5, 5), (0, 10), (2.5, 5)]),
    ((0, 0), 10, 10, 0.7, [(0, 0), (-5, 7), (0, 10), (5, 7)]),
    ((1, 1), 10, 10, 0.5, [(1, 1), (-4, 6), (1, 11), (6, 6)]),
    ((-1, -1), 10, 10, 0.5, [(-1, -1), (-6, 4), (-1, 9), (4, 4)]),
    ((0, 0), 10, 10, 1.5, [(0, 0), (-5, 15), (0, 10), (5, 15)]),
]


def test_is_polygon_subclass():
    assert issubclass(Kite, Polygon)


@pytest.mark.parametrize(
    "coordinates",
    [
        ((0, 0), (0, 2), (1, 0)),
        ((0, 0), (0, 2)),
        ((0, 0),),
        ((0, 0), (0, 2), (1, 0), (1, 3), (1, 4)),
    ],
)
def test_kite_requires_four_vertices(coordinates):
    with pytest.raises(ValueError, match="vertices must contain exactly 4 points."):
        Kite(vertices=coords_iterable_to_vertices(coordinates))


def test_corner_vertices_indices():
    kite = Kite(vertices=(Vec2D(0, 0), Vec2D(1, 1), Vec2D(0, 2), Vec2D(-1, 1)))

    assert kite.corner_vertices_indices == (0, 1, 2, 3)


@pytest.mark.parametrize(
    [
        "origin",
        "height",
        "width",
        "diagonal_intersection_along_height",
        "expected_coords",
    ],
    KITE_DIMENSIONS_PARAMS,
)
def test_calculate_kite_corner_vertices(
    origin, height, width, diagonal_intersection_along_height, expected_coords
):
    actual = Kite.calculate_kite_corner_vertices(
        origin=Vec2D(*origin),
        height=height,
        width=width,
        diagonal_intersection_along_height=diagonal_intersection_along_height,
    )

    expected = coords_iterable_to_vertices(expected_coords)

    assert actual == expected


@pytest.mark.parametrize(
    [
        "origin",
        "height",
        "width",
        "diagonal_intersection_along_height",
        "expected_coords",
    ],
    KITE_DIMENSIONS_PARAMS,
)
def test_from_origin_and_dimensions(
    origin, height, width, diagonal_intersection_along_height, expected_coords
):
    actual = Kite.from_origin_and_dimensions(
        origin=Vec2D(*origin),
        height=height,
        width=width,
        diagonal_intersection_along_height=diagonal_intersection_along_height,
    )

    expected_vertices = coords_iterable_to_vertices(expected_coords)

    expected = Kite(vertices=expected_vertices)

    assert actual == expected


def test_can_initialise_non_convex_kite():
    kite = Kite.from_origin_and_dimensions(
        origin=Vec2D(0, 5), height=10, width=5, diagonal_intersection_along_height=1.1
    )

    assert not kite.is_convex()


@pytest.mark.parametrize(
    "diagonal_intersection_along_height",
    [
        5.0,
        3.0,
        1.5,
        1.2,
        1.01,
        1.0,
        0.99,
        0.5,
        0.1,
        0.0,
        -0.5,
        -0.99,
        -1.0,
        -1.01,
        -1.2,
        -4.0,
    ],
)
def test_diagonal_intersection_along_height_range_zero_one_convex(
    diagonal_intersection_along_height,
):
    """Test 0 <= diagonal_intersection_along_height <= 1 defines convex kites."""

    kite = Kite.from_origin_and_dimensions(
        origin=Vec2D(0, 5),
        height=10,
        width=5,
        diagonal_intersection_along_height=diagonal_intersection_along_height,
    )

    if 0 <= diagonal_intersection_along_height <= 1:
        assert kite.is_convex()

    else:
        assert not kite.is_convex()


class TestEq:
    """Tests for the __eq__ method."""

    @pytest.mark.parametrize(
        "coordinates",
        [((0, 0), (0, 2), (1, 0), (1, 3)), ((-5, 0), (-10, 2), (-4, 9), (1, 3))],
    )
    def test_kites_equal(self, coordinates):
        a = Kite(vertices=coords_iterable_to_vertices(coordinates))
        b = Kite(vertices=coords_iterable_to_vertices(coordinates))

        assert a == b

    @pytest.mark.parametrize("angle", [360, 720])
    @pytest.mark.parametrize(
        "coordinates",
        [((0, 0), (0, 2), (1, 0), (1, 3)), ((-5, 0), (-10, 2), (-4, 9), (1, 3))],
    )
    def test_kites_equal_under_complete_rotation(self, coordinates, angle):
        a = Kite(vertices=coords_iterable_to_vertices(coordinates))
        b = Kite(vertices=coords_iterable_to_vertices(coordinates)).rotate(
            angle=angle, about_point=Vec2D(-3, -3)
        )

        assert a == b

    def test_kites_equal_not_equal(self):
        coords_a = ((0, 0), (0, 2), (1, 0), (1, 3))
        coords_b = ((-5, 0), (-10, 2), (-4, 9), (1, 3))

        a = Kite(vertices=coords_iterable_to_vertices(coords_a))
        b = Kite(vertices=coords_iterable_to_vertices(coords_b))

        assert a != b

    @pytest.mark.parametrize(
        "coordinates",
        [((0, 0), (0, 2), (1, 0), (1, 3)), ((-5, 0), (-10, 2), (-4, 9), (1, 3))],
    )
    def test_kites_equal_not_equal_under_translation(self, coordinates):
        vertices = coords_iterable_to_vertices(coordinates)
        vertices_translated = tuple(vertex + Vec2D(1, 2) for vertex in vertices)

        a = Kite(vertices=vertices)
        b = Kite(vertices=vertices_translated)

        assert a != b

    @pytest.mark.parametrize(
        "coordinates",
        [((0, 0), (0, 2), (1, 0), (1, 3)), ((-5, 0), (-10, 2), (-4, 9), (1, 3))],
    )
    def test_kites_equal_not_equal_under_rotation(self, coordinates):
        vertices = coords_iterable_to_vertices(coordinates)

        a = Kite(vertices=vertices)
        b = Kite(vertices=vertices).rotate(angle=45, about_point=Vec2D(0, 0))

        assert a != b


class TestGetHeight:
    """Tests for the Kite.get_height method."""

    @pytest.mark.parametrize(
        ["coordinates", "expected"],
        [
            (((0, 0), (-5, 5), (0, 10), (5, 5)), 10),
            (((-2, -2), (-4, 0), (-2, 9), (3, 3)), 11),
            (((0, 0), (-5, 5), (1, 10), (5, 5)), sqrt(101)),
        ],
    )
    def test_expected_height(self, coordinates, expected):
        vertices = coords_iterable_to_vertices(coordinates)

        kite = Kite(vertices=vertices)

        assert kite.get_height() == expected

    @pytest.mark.parametrize("diagonal_intersection_along_height", [-0.5, 0.4, 1.2])
    @pytest.mark.parametrize("height", [10, 5, 2.5])
    def test_height_matches_height_from_initialisation(
        self, height, diagonal_intersection_along_height
    ):
        kite = Kite.from_origin_and_dimensions(
            origin=Vec2D(0, 5),
            height=height,
            width=5,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
        )

        assert kite.get_height() == height

    @pytest.mark.parametrize("about_point", [Vec2D(3, 4), Vec2D(-1, 0)])
    @pytest.mark.parametrize("angle", [77, 190])
    def test_height_unchanged_under_rotation(self, angle, about_point):
        height = 10

        kite = Kite.from_origin_and_dimensions(
            origin=Vec2D(0, 5),
            height=height,
            width=5,
            diagonal_intersection_along_height=0.5,
        ).rotate(angle=angle, about_point=about_point)

        assert pytest.approx(kite.get_height()) == height


class TestGetWidth:
    """Tests for the Kite.get_width method."""

    @pytest.mark.parametrize(
        ["coordinates", "expected"],
        [
            (((0, 0), (-5, 5), (0, 10), (5, 5)), 10),
            (((-2, -2), (-4, 0), (-2, 9), (3, 3)), sqrt(49 + 9)),
        ],
    )
    def test_expected_width(self, coordinates, expected):
        vertices = coords_iterable_to_vertices(coordinates)

        kite = Kite(vertices=vertices)

        assert kite.get_width() == expected

    @pytest.mark.parametrize("diagonal_intersection_along_height", [-0.2, 0.7, 1.1])
    @pytest.mark.parametrize("width", [10, 5, 2.5])
    def test_width_matches_height_from_initialisation(
        self, width, diagonal_intersection_along_height
    ):
        kite = Kite.from_origin_and_dimensions(
            origin=Vec2D(0, 5),
            height=6,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
        )

        assert kite.get_width() == width

    @pytest.mark.parametrize("about_point", [Vec2D(0, -2), Vec2D(1, 3)])
    @pytest.mark.parametrize("angle", [13, 268])
    def test_width_unchanged_under_rotation(self, angle, about_point):
        width = 8

        kite = Kite.from_origin_and_dimensions(
            origin=Vec2D(0, 5),
            height=10,
            width=width,
            diagonal_intersection_along_height=0.5,
        ).rotate(angle=angle, about_point=about_point)

        assert pytest.approx(kite.get_width()) == width
