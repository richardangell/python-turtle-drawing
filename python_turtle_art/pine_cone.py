from turtle import Turtle, Vec2D
from math import cos, sin

from helpers import convert_degrees_to_radians
from kite import CurvedConvexKite, CurvedConvexKiteFactory
from body_part import BodyPart


class PineCone:
    """Class for drawing pine cone."""

    def __init__(
        self,
        outer_kite: CurvedConvexKite,
        inner_kite_factory: CurvedConvexKiteFactory,
        outer_kite_line_width: int = 5,
        horizontal_offset: int = 5,
        vertical_offset: int = 5,
        inner_kite_fill: bool = True,
        inner_kite_colour: str = "white",
        initial_body_parts: tuple[BodyPart, ...] = (),
        final_body_parts: tuple[BodyPart, ...] = (),
    ):
        self.outer_kite = outer_kite
        self.inner_kite_factory = inner_kite_factory
        self.outer_kite_line_width = outer_kite_line_width
        self.horizontal_offset = horizontal_offset
        self.vertical_offset = vertical_offset
        self.inner_kite_fill = inner_kite_fill
        self.inner_kite_colour = inner_kite_colour
        self.initial_body_parts = initial_body_parts
        self.final_body_parts = final_body_parts

    def draw(self, turtle: Turtle):
        """Draw the pine cone."""

        self._draw_initial_body_parts(turtle)

        self.outer_kite.draw(turtle=turtle, fill=True, colour="black")

        if self.inner_kite_factory.height is None:
            raise ValueError("inner_kite_factory.height not specified")
        else:
            inner_kite_factory_height = self.inner_kite_factory.height

        if self.inner_kite_factory.width is None:
            raise ValueError("inner_kite_factory.width not specified")
        else:
            inner_kite_factory_half_width = self.inner_kite_factory.width / 2

        if self.inner_kite_factory.diagonal_intersection_along_height is None:
            raise ValueError(
                "inner_kite_factory.diagonal_intersection_along_height not specified"
            )
        else:
            inner_kite_factory_diagonal_intersection_along_height = (
                self.inner_kite_factory.diagonal_intersection_along_height
            )

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
                * (self.inner_kite_factory.height + 2 * self.vertical_offset)
                * unit_vector_vertical_move
            )

            self.inner_kite_factory.get_kite(origin=center_origin).draw(
                turtle=turtle, fill=self.inner_kite_fill, colour=self.inner_kite_colour
            )

            center_origin_half_row_up = (
                center_origin
                + (
                    self.vertical_offset
                    + inner_kite_factory_diagonal_intersection_along_height
                    * inner_kite_factory_height
                )
                * unit_vector_vertical_move
            )

            half_row_up_half_horizontal_move = (
                self.inner_kite_factory.width + self.horizontal_offset
            ) / 2

            half_row_up_half_negative_horizontal_move = (
                self.inner_kite_factory.width + self.horizontal_offset
            ) / 2

            # fill out row right from the center
            for i in range(n_side_inner_kites):
                offset_origin = (
                    center_origin
                    + (i + 1)
                    * (self.inner_kite_factory.width + self.horizontal_offset)
                    * unit_vector_horizontal_move
                )

                self.inner_kite_factory.get_kite(origin=offset_origin).draw(
                    turtle=turtle,
                    fill=self.inner_kite_fill,
                    colour=self.inner_kite_colour,
                )

                offset_origin_half_row_up = (
                    center_origin_half_row_up
                    + (
                        half_row_up_half_horizontal_move
                        + i * (self.inner_kite_factory.width + self.horizontal_offset)
                    )
                    * unit_vector_horizontal_move
                )

                self.inner_kite_factory.get_kite(origin=offset_origin_half_row_up).draw(
                    turtle=turtle,
                    fill=self.inner_kite_fill,
                    colour=self.inner_kite_colour,
                )

            # fill out row left from the center
            for i in range(n_side_inner_kites):
                offset_origin = (
                    center_origin
                    - (i + 1)
                    * (self.inner_kite_factory.width + self.horizontal_offset)
                    * unit_vector_horizontal_move
                )

                self.inner_kite_factory.get_kite(origin=offset_origin).draw(
                    turtle=turtle,
                    fill=self.inner_kite_fill,
                    colour=self.inner_kite_colour,
                )

                offset_origin_half_row_up = (
                    center_origin_half_row_up
                    - (
                        half_row_up_half_negative_horizontal_move
                        + i * (self.inner_kite_factory.width + self.horizontal_offset)
                    )
                    * unit_vector_horizontal_move
                )

                self.inner_kite_factory.get_kite(origin=offset_origin_half_row_up).draw(
                    turtle=turtle,
                    fill=self.inner_kite_fill,
                    colour=self.inner_kite_colour,
                )

        self.outer_kite.draw(
            turtle=turtle, fill=False, colour="black", size=self.outer_kite_line_width
        )

        self._draw_final_body_parts(turtle)

    def _draw_initial_body_parts(self, turtle: Turtle):
        for body_part in self.initial_body_parts:
            body_part.draw(turtle)

    def _draw_final_body_parts(self, turtle: Turtle):
        for body_part in self.final_body_parts:
            body_part.draw(turtle)
