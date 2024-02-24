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

        if self.inner_kite_factory.height is None:
            raise ValueError("inner_kite_factory.height not specified")
        else:
            inner_kite_factory_height = self.inner_kite_factory.height

        if self.inner_kite_factory.width is None:
            raise ValueError("inner_kite_factory.width not specified")
        else:
            inner_kite_factory_half_width = self.inner_kite_factory.width / 2

        # number of inner kites to be drawn either side of the vertical bisector
        n_side_inner_kites = (
            int(
                (self.outer_kite.half_width - inner_kite_factory_half_width)
                // self.inner_kite_factory.width
            )
            + 1
        )

        n_rows_inner_kites = (
            int(self.outer_kite.height // inner_kite_factory_height) + 1
        )

        inner_angle = convert_degrees_to_radians(self.outer_kite.rotation)

        vertical_y_component = self.outer_kite.height * cos(inner_angle)
        vertical_x_component = self.outer_kite.height * sin(inner_angle)

        horizontal_x_component = self.outer_kite.width * cos(inner_angle)
        horizontal_y_component = -self.outer_kite.width * sin(inner_angle)

        unit_vector_vertical_move = Vec2D(
            x=vertical_x_component / self.outer_kite.height,
            y=vertical_y_component / self.outer_kite.height,
        )

        unit_vector_horizontal_move = Vec2D(
            x=horizontal_x_component / self.outer_kite.width,
            y=horizontal_y_component / self.outer_kite.width,
        )

        for row_number in range(n_rows_inner_kites):
            center_origin = (
                self.outer_kite.origin
                + row_number
                * self.inner_kite_factory.height
                * unit_vector_vertical_move
            )

            inner_kite = self.inner_kite_factory.get_kite(origin=center_origin)

            inner_kite.draw(turtle=turtle, fill=False, colour="black")

            # fill out row right from the center
            for i in range(n_side_inner_kites):
                offset_origin = (
                    center_origin
                    + (i + 1)
                    * self.inner_kite_factory.width
                    * unit_vector_horizontal_move
                )

                inner_kite = self.inner_kite_factory.get_kite(origin=offset_origin)

                inner_kite.draw(turtle=turtle, fill=False, colour="black")

            # fill out row left from the center
            for i in range(n_side_inner_kites):
                offset_origin = (
                    center_origin
                    - (i + 1)
                    * self.inner_kite_factory.width
                    * unit_vector_horizontal_move
                )

                inner_kite = self.inner_kite_factory.get_kite(origin=offset_origin)

                inner_kite.draw(turtle=turtle, fill=False, colour="black")

        self.outer_kite.draw(turtle=turtle, fill=False, colour="black")
