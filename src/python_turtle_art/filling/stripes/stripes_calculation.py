from collections import namedtuple
from collections.abc import Sequence
from turtle import Vec2D
from warnings import warn

from ...lines.line import Line
from ...lines.line_intersection import (
    get_horizontal_intersection_of_line,
    get_vertical_intersection_of_line,
)
from ...polygons.convex_polygon import ConvexPolygon
from ...vertices.vertices import Axis

StepsBetweenIndices = namedtuple("StepsBetweenIndices", ["a_to_b", "b_to_a"])


def get_number_of_steps_between_indices(
    index_a: int, index_b: int, sequence: Sequence
) -> StepsBetweenIndices:
    """Calculate number of indexes between two indices in a sequence, wrapping the end.

    Args:
        index_a (int): first index.
        index_b (int): second index.
        sequence (Sequence): list of items.

    """
    n = len(sequence)

    if index_a < index_b:
        number_steps_a_to_b = index_b - index_a
        number_steps_b_to_a = n - index_b + index_a
    else:
        number_steps_a_to_b = n - index_a + index_b
        number_steps_b_to_a = index_a - index_b

    return StepsBetweenIndices(a_to_b=number_steps_a_to_b, b_to_a=number_steps_b_to_a)


def get_incremenets_from_origin_within_range(
    origin: int, increment: int, min_: int | float, max_: int | float
):
    """Get increments from origin that fall within a range.

    Args:
        origin (int): starting point, multiples of increment will be calculated from
            the origin value.
        increment (int): distance between each increment.
        min_ (int | float): minimum value of the range.
        max_ (int | float): maximum value of the range.

    """

    if increment <= 0:
        raise ValueError("Increment must be greater than zero.")

    start = int(((min_) // increment) * increment)
    stop = int((((max_) // increment) + 1) * increment)

    increment_remainder = origin % increment

    increments_in_range = [
        x
        for x in range(
            start + increment_remainder, stop + increment_remainder + 1, increment
        )
        if min_ < x < max_
    ]

    if len(increments_in_range) == 0:
        warn(
            message=f"No increments of {increment} in range {min_} to "
            f"{max_}, starting from {origin}.",
            stacklevel=1,
        )

    return increments_in_range


def get_filling_lines(
    origin: int, gap: int, polygon: ConvexPolygon, axis: int = 0
) -> list[Line]:
    """Get the horizontal or vertical stripes to fill a convex polygon."""

    axis_enum = Axis(axis)

    if axis_enum == Axis.x:
        intersection_function = get_vertical_intersection_of_line
    else:
        intersection_function = get_horizontal_intersection_of_line

    extreme_indices = polygon.get_vertices_indices_with_min_and_max_values_on_axis(
        axis=axis
    )
    min_index = extreme_indices.minimum
    max_index = extreme_indices.maximum

    if min_index == max_index:
        raise ValueError("Polygon has no area to fill.")

    min_ = polygon.vertices[min_index][axis]
    max_ = polygon.vertices[max_index][axis]

    stripe_values_on_axis = get_incremenets_from_origin_within_range(
        origin=origin, increment=gap, min_=min_, max_=max_
    )

    number_steps = get_number_of_steps_between_indices(
        index_a=min_index, index_b=max_index, sequence=polygon.vertices
    )
    number_steps_min_to_max = number_steps.a_to_b
    number_steps_max_to_min = number_steps.b_to_a

    stipe_counter = 0

    stripe_points_at_each_value: dict[int, list[Vec2D]] = {
        i: [] for i in range(len(stripe_values_on_axis))
    }

    for upward_step in range(number_steps_min_to_max):
        index = (upward_step + min_index) % len(polygon.vertices)
        next_index = (upward_step + min_index + 1) % len(polygon.vertices)

        current_vertex = polygon.vertices[index]
        next_vertex = polygon.vertices[next_index]

        while (stipe_counter < len(stripe_values_on_axis)) and (
            current_vertex[axis]
            < stripe_values_on_axis[stipe_counter]
            <= next_vertex[axis]
        ):
            intersection_point = intersection_function(
                p0=current_vertex,
                p1=next_vertex,
                constant=stripe_values_on_axis[stipe_counter],
            )

            stripe_points_at_each_value[stipe_counter].append(intersection_point)

            stipe_counter += 1

    for stripe_index, stripe_points in stripe_points_at_each_value.items():
        if len(stripe_points) != 1:
            raise ValueError(
                f"Horizontal stripe {stripe_index} does not have one vertex."
            )

    if stipe_counter != len(stripe_values_on_axis):
        raise ValueError("Did not find all horizontal stripes.")

    stipe_counter -= 1

    for downward_step in range(number_steps_max_to_min):
        index = (downward_step + max_index) % len(polygon.vertices)
        next_index = (downward_step + max_index + 1) % len(polygon.vertices)

        current_vertex = polygon.vertices[index]
        next_vertex = polygon.vertices[next_index]

        while (stipe_counter >= 0) and (
            next_vertex[axis]
            < stripe_values_on_axis[stipe_counter]
            <= current_vertex[axis]
        ):
            intersection_point = intersection_function(
                p0=current_vertex,
                p1=next_vertex,
                constant=stripe_values_on_axis[stipe_counter],
            )

            stripe_points_at_each_value[stipe_counter].append(intersection_point)

            stipe_counter -= 1

    for stripe_index, stripe_points in stripe_points_at_each_value.items():
        if len(stripe_points) != 2:
            raise ValueError(
                f"Horizontal stripe {stripe_index} does not have two vertices."
            )

    stripe_lines = [
        Line(vertices=tuple(stripe_points))
        for stripe_points in stripe_points_at_each_value.values()
    ]

    return stripe_lines
