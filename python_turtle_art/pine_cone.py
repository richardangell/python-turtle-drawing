from turtle import Turtle, Vec2D
from math import cos, sin

from helpers import convert_degrees_to_radians
from kite import CurvedConvexKite, CurvedConvexKiteFactory


class PineCone:
    """Class for drawing pine cone."""

    def __init__(
        self, outer_kite: CurvedConvexKite, inner_kite_factory: CurvedConvexKiteFactory
    ):
        self.outer_kite = outer_kite
        self.inner_kite_factory = inner_kite_factory

    def draw(self, turtle: Turtle):
        """Draw the pine cone."""

        self.outer_kite.draw(turtle=turtle, fill=False, colour="black")

        # inner_kite_factory_half_width = self.inner_kite_factory.width / 2

        # number of inner kites to be drawn either side of the vertical bisector
        # n_side_inner_kites = (
        #    self.outer_kite.half_width - inner_kite_factory_half_width
        # ) // self.inner_kite_factory.width + 1

        if self.inner_kite_factory.height is None:
            raise ValueError("inner_kite_factory.height not specified")
        else:
            inner_kite_factory_height = self.inner_kite_factory.height

        n_rows_inner_kites = (
            int(self.outer_kite.height // inner_kite_factory_height) + 1
        )

        inner_angle = convert_degrees_to_radians(self.outer_kite.rotation)

        vertical_distance = self.outer_kite.height * cos(inner_angle)

        horizontal_distance = self.outer_kite.height * sin(inner_angle)

        unit_distance_in_angle_direction = Vec2D(
            x=horizontal_distance / self.outer_kite.height,
            y=vertical_distance / self.outer_kite.height,
        )

        for row_number in range(n_rows_inner_kites):
            center_origin = (
                self.outer_kite.origin
                + row_number
                * self.inner_kite_factory.height
                * unit_distance_in_angle_direction
            )

            inner_kite = self.inner_kite_factory.get_kite(origin=center_origin)

            inner_kite.draw(turtle=turtle, fill=False, colour="black")

        self.outer_kite.draw(turtle=turtle, fill=False, colour="black")
