from collections import namedtuple
from collections.abc import Sequence
from turtle import Turtle, Vec2D
from warnings import warn

from ..lines.line import Line
from ..lines.line_intersection import get_horizontal_intersection_of_line
from ..polygons.convex_polygon import BaseConvexFill, ConvexPolygon


class HorizontalStipeFill(BaseConvexFill):
    """Fill a convex polygon with horizontal stripes.

    Args:
        gap (int): distance between each stripe.
        origin (int): y-coordinate of the origin horizontal stripes will be drawn
            relative to.

    """

    def __init__(self, gap: int, colour: str = "black", origin: int = 0):
        self.gap = gap
        self.colour = colour
        self.origin = origin

    def fill(self, turtle: Turtle, polygon: ConvexPolygon):
        """Fill a convex polygon with horizontal stipes.

        Args:
            turtle (Turtle): turtle graphics object.
            polygon (ConvexPolygon): convex polygon to fill.

        """
        stripes = self._get_horizontal_stipe_lines(polygon=polygon)

        for stripe in stripes:
            stripe.draw(turtle=turtle, size=5)

    def _get_horizontal_stipe_lines(self, polygon: ConvexPolygon) -> list[Line]:
        extreme_indices = polygon.get_extreme_y_vertices_indices()
        min_y_index = extreme_indices.minimum
        max_y_index = extreme_indices.maximum

        if min_y_index == max_y_index:
            raise ValueError("Polygon has no area to fill.")

        min_y = polygon.vertices[min_y_index][1]
        max_y = polygon.vertices[max_y_index][1]

        horizontal_line_y = get_incremenets_from_origin_within_range(
            origin=self.origin, increment=self.gap, min_=min_y, max_=max_y
        )

        number_steps = get_number_of_steps_between_indices(
            index_a=min_y_index, index_b=max_y_index, sequence=polygon.vertices
        )
        number_steps_min_to_max = number_steps.a_to_b
        number_steps_max_to_min = number_steps.b_to_a

        horizontal_stipe_counter = 0

        horizontal_stripe_points: dict[int, list[Vec2D]] = {
            i: [] for i in range(len(horizontal_line_y))
        }

        for upward_step in range(number_steps_min_to_max):
            index = (upward_step + min_y_index) % len(polygon.vertices)
            next_index = (upward_step + min_y_index + 1) % len(polygon.vertices)

            current_vertex = polygon.vertices[index]
            next_vertex = polygon.vertices[next_index]

            while (horizontal_stipe_counter < len(horizontal_line_y)) and (
                current_vertex[1]
                < horizontal_line_y[horizontal_stipe_counter]
                <= next_vertex[1]
            ):
                intersection_point = get_horizontal_intersection_of_line(
                    p0=current_vertex,
                    p1=next_vertex,
                    horizontal_y=horizontal_line_y[horizontal_stipe_counter],
                )

                horizontal_stripe_points[horizontal_stipe_counter].append(
                    intersection_point
                )

                horizontal_stipe_counter += 1

        for stripe_index, stripe_points in horizontal_stripe_points.items():
            if len(stripe_points) != 1:
                raise ValueError(
                    f"Horizontal stripe {stripe_index} does not have one vertex."
                )

        if horizontal_stipe_counter != len(horizontal_line_y):
            raise ValueError("Did not find all horizontal stripes.")

        horizontal_stipe_counter -= 1

        for downward_step in range(number_steps_max_to_min):
            index = (downward_step + max_y_index) % len(polygon.vertices)
            next_index = (downward_step + max_y_index + 1) % len(polygon.vertices)

            current_vertex = polygon.vertices[index]
            next_vertex = polygon.vertices[next_index]

            while (horizontal_stipe_counter < len(horizontal_line_y)) and (
                next_vertex[1]
                < horizontal_line_y[horizontal_stipe_counter]
                <= current_vertex[1]
            ):
                intersection_point = get_horizontal_intersection_of_line(
                    p0=current_vertex,
                    p1=next_vertex,
                    horizontal_y=horizontal_line_y[horizontal_stipe_counter],
                )

                horizontal_stripe_points[horizontal_stipe_counter].append(
                    intersection_point
                )

                horizontal_stipe_counter -= 1

        for stripe_index, stripe_points in horizontal_stripe_points.items():
            if len(stripe_points) != 2:
                raise ValueError(
                    f"Horizontal stripe {stripe_index} does not have two vertices."
                )

        stripe_lines = [
            Line(vertices=tuple(stripe_points))
            for stripe_points in horizontal_stripe_points.values()
        ]

        return stripe_lines


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

    start = int((min_ // increment) * increment)
    stop = int((max_ // increment) * increment)

    increments_in_range = [x for x in range(start, stop, increment) if min_ < x < max_]

    if len(increments_in_range) == 0:
        warn(
            message=f"No increments of {increment} in range {min_} to "
            f"{max_}, starting from {origin}.",
            stacklevel=1,
        )

    return increments_in_range
