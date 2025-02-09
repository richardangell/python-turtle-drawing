from turtle import Turtle, Vec2D
from typing import Optional, Self, Union

from ..helpers.rotation import rotate_about_point
from ..helpers.turtle import jump_to


class Polygon:
    """Class for drawing an arbitrary polygon.

    Args:
        vertices (tuple[Vec2D, ...]): Points of the polygon. At least 3 must be
            supplied.

    """

    def __init__(self, vertices: tuple[Vec2D, ...]):
        self.vertices = vertices

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Set vertices attribute and check there are at least 3 points."""
        if len(vertices) < 3:
            raise ValueError("vertices must contain at least 3 points.")
        self._vertices = vertices

    def draw(self, turtle: Turtle, colour: str = "black", size: Optional[int] = None):
        """Set pensize and colour then draw polygon edges."""

        original_colour = turtle.pencolor()
        original_pensize = turtle.pensize()

        turtle.color(colour)
        turtle.pensize(size)

        jump_to(turtle=turtle, position=self._vertices[-1])

        for point in self._vertices:
            turtle.goto(point)

        turtle.color(original_colour)
        turtle.pensize(original_pensize)

    def rotate(self, angle: Union[int, float], about_point: Vec2D) -> Self:
        """Rotate polygon.

        Args:
            angle (Union[int, float]): angle to rotate the polygon.
            about_point (Vec2D): point to rotate about.

        """
        if (angle % 360) != 0:
            self.vertices = tuple(
                rotate_about_point(point, angle, about_point) for point in self.vertices
            )

        return self

    def is_convex(self) -> bool:
        """Check if the polygon is convex.

        For a polygon to be convex there must be exactly 2 flips in the direction of x
        and y coordinates as we traverse around each vertex. The interrior angles must
        all be less than or equal to 180 degrees.

        Algorithm from https://math.stackexchange.com/a/1745427.

        The perp dot product; https://mathworld.wolfram.com/PerpDotProduct.html is used
        to below (`w = bx * ay - ax * by`) to check that the 'orientation' of
        consecutive pairs of edges does not change.

        The perp dot producct is the cross product (`cx = ay * bz - az * by`,
        `cy = az * bx - ay * bz` and `cz = ax * by - ay * bx`) of the 2d vectors only
        keeping the z-component - as we only care about the direction of this
        component. https://www.reddit.com/r/learnmath/comments/agfm8g/comment/ee5ymer/
        has slightly more discussion.

        See annimation here; https://en.wikipedia.org/wiki/Cross_product#Direction for
        how the cross product flips direction when the angle between vectors moves from
        < 180 degrees to > 180 degrees.

        Note that the implementation below has the signs flipped (i.e.
        `cz = ay * bx - ax * by`) compared to the above defintion so that both vectors
        are pointing out from the same point rather than the first vector pointing to
        the start of the second vector.

        """

        w_sign = 0.0  # First nonzero orientation (positive or negative)

        x_sign = 0
        x_first_sign = 0  # Sign of first nonzero edge vector x
        x_flips = 0  # Number of sign changes in x

        y_sign = 0
        y_first_sign = 0  # Sign of first nonzero edge vector y
        y_flips = 0  # Number of sign changes in y

        curr = self.vertices[-2]  # Second-to-last vertex
        next = self.vertices[-1]  # Last vertex

        for v in self.vertices:  # Each vertex, in order
            prev = curr  # Previous vertex
            curr = next  # Current vertex
            next = v  # Next vertex

            # Previous edge vector ("before"):
            bx = curr[0] - prev[0]
            by = curr[1] - prev[1]

            # Next edge vector ("after"):
            ax = next[0] - curr[0]
            ay = next[1] - curr[1]

            # Calculate sign flips using the next edge vector ("after"),
            # recording the first sign.
            if ax > 0:
                if x_sign == 0:
                    x_first_sign = 1
                elif x_sign < 0:
                    x_flips += 1
                x_sign = 1
            elif ax < 0:
                if x_sign == 0:
                    x_first_sign = -1
                elif x_sign > 0:
                    x_flips += 1
                x_sign = -1

            if x_flips > 2:
                return False

            if ay > 0:
                if y_sign == 0:
                    y_first_sign = 1
                elif y_sign < 0:
                    y_flips += 1
                y_sign = 1
            elif ay < 0:
                if y_sign == 0:
                    y_first_sign = -1
                elif y_sign > 0:
                    y_flips += 1
                y_sign = -1

            if y_flips > 2:
                return False

            # Find out the orientation of this pair of edges,
            # and ensure it does not differ from previous ones.
            w = bx * ay - ax * by
            if (w_sign == 0) and (w != 0):
                w_sign = w
            elif (w_sign > 0) and (w < 0) or (w_sign < 0) and (w > 0):
                return False

        # Final/wraparound sign flips:
        if (x_sign != 0) and (x_first_sign != 0) and (x_sign != x_first_sign):
            x_flips += 1
        if (y_sign != 0) and (y_first_sign != 0) and (y_sign != y_first_sign):
            y_flips += 1

        # Convex polygons have two sign flips along each axis.
        return (x_flips == 2) and (y_flips == 2)
