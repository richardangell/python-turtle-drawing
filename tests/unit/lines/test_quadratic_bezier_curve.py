from math import sqrt
from turtle import Vec2D

import pytest

from python_turtle_art.lines.offset_from_line import OffsetFromLine
from python_turtle_art.lines.quadratic_bezier_curve import QuadraticBezierCurve


def test_cannot_initalise_with_one_step():
    with pytest.raises(ValueError, match="vertices must contain at least 2 points."):
        QuadraticBezierCurve.from_start_and_end(
            start=Vec2D(0, 0), end=Vec2D(10, 0), off_line=None, steps=1
        )


def test_error_if_start_equals_end():
    with pytest.raises(
        ValueError, match="Can only create curve between two different points."
    ):
        QuadraticBezierCurve.from_start_and_end(
            start=Vec2D(0, 0), end=Vec2D(0, 0), off_line=None, steps=5
        )


@pytest.mark.parametrize(
    "offset",
    [
        None,
        OffsetFromLine(0.5, 10),
    ],
)
def test_curve_with_two_steps_is_start_and_end_only(offset):
    start = Vec2D(0, 0)
    end = Vec2D(10, 0)

    curve = QuadraticBezierCurve.from_start_and_end(
        start=start, end=end, off_line=offset, steps=2
    )

    assert len(curve.vertices) == 2

    assert curve.vertices[0] == start
    assert curve.vertices[1] == end


@pytest.mark.parametrize("steps", [3, 5, 10])
def test_first_and_last_vertices_are_start_and_end(steps):
    start = Vec2D(4, 5)
    end = Vec2D(10, -9)

    curve = QuadraticBezierCurve.from_start_and_end(
        start=start, end=end, off_line=OffsetFromLine(0.5, 10), steps=steps
    )

    assert curve.vertices[0] == start
    assert curve.vertices[-1] == end


@pytest.mark.parametrize("steps", [3, 5, 10])
def test_vertices_are_unique(steps):
    curve = QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(0, 0),
        end=Vec2D(10, 0),
        off_line=OffsetFromLine(0.5, 10),
        steps=steps,
    )

    assert len(set(curve.vertices)) == len(curve.vertices)


@pytest.mark.parametrize("steps", [3, 8, 21])
def test_number_vertices_equal_to_steps(steps):
    curve = QuadraticBezierCurve.from_start_and_end(
        start=Vec2D(0, 0),
        end=Vec2D(10, 0),
        off_line=OffsetFromLine(0.5, 10),
        steps=steps,
    )

    assert len(curve.vertices) == steps


@pytest.mark.parametrize(
    ["control_point_distance", "expected_counts_in_quadrants"],
    [
        (sqrt(2 * 25), [18, 0, 0, 0]),
        (sqrt(2 * 50), [8, 5, 5, 0]),
        (sqrt(2 * 75), [2, 8, 8, 0]),
        (sqrt(2 * 100), [0, 9, 9, 0]),
        (sqrt(2 * 150), [0, 7, 7, 4]),
        (sqrt(2 * 300), [0, 5, 5, 8]),
        (sqrt(2 * 1000), [0, 3, 3, 12]),
    ],
)
def test_control_point_further_away_pulls_points_further_from_start_end(
    control_point_distance, expected_counts_in_quadrants
):
    start = Vec2D(10, 0)
    end = Vec2D(0, 10)

    off_line = OffsetFromLine(0.5, control_point_distance)

    curve = QuadraticBezierCurve.from_start_and_end(
        start=start, end=end, off_line=off_line, steps=20
    )

    count_points_x_gt_0_y_gt_0 = 0
    count_points_x_gt_0_y_lt_0 = 0
    count_points_x_lt_0_y_gt_0 = 0
    count_points_x_lt_0_y_lt_0 = 0

    for vertex in curve.vertices[1:-1]:
        if vertex[0] > 0 and vertex[1] > 0:
            count_points_x_gt_0_y_gt_0 += 1
        elif vertex[0] > 0 and vertex[1] < 0:
            count_points_x_gt_0_y_lt_0 += 1
        elif vertex[0] < 0 and vertex[1] > 0:
            count_points_x_lt_0_y_gt_0 += 1
        else:
            count_points_x_lt_0_y_lt_0 += 1

    actual = [
        count_points_x_gt_0_y_gt_0,
        count_points_x_gt_0_y_lt_0,
        count_points_x_lt_0_y_gt_0,
        count_points_x_lt_0_y_lt_0,
    ]

    assert actual == expected_counts_in_quadrants


def test_control_point_with_zero_offset_produces_points_on_straight_line():
    start = Vec2D(0, 0)
    end = Vec2D(10, 10)

    off_line = OffsetFromLine(0.5, 0)

    curve = QuadraticBezierCurve.from_start_and_end(
        start=start, end=end, off_line=off_line, steps=20
    )

    for vertex in curve.vertices[1:-1]:
        assert 0 < vertex[0] < 10
        assert 0 < vertex[1] < 10
        assert vertex[0] == vertex[1]


def test_default_control_point_produces_points_on_straight_line():
    start = Vec2D(0, 0)
    end = Vec2D(10, 10)

    curve = QuadraticBezierCurve.from_start_and_end(start=start, end=end, steps=20)

    for vertex in curve.vertices[1:-1]:
        assert 0 < vertex[0] < 10
        assert 0 < vertex[1] < 10
        assert vertex[0] == vertex[1]
