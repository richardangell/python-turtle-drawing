from turtle import Turtle, Vec2D
from math import cos, sin
import random

from helpers import convert_degrees_to_radians, rotate_about_point
from kite import CurvedConvexKite, CurvedConvexKiteFactory
from body_part import BodyPart
from body import Limb
from line import OffsetFromLine
from face import CurvedMouth, Eyes


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


class RandomPineConeFactory:
    def __init__(
        self,
        origin: Vec2D,
        height_range: tuple[int, int] = (50, 70),
        seed: int = 0,
    ):
        self.origin = origin
        self.height_range = height_range
        self.seed = seed

        random.seed(seed)

        self._outer_kite_rotation = random.randint(0, 360)
        self._inner_kite_rotation = self._outer_kite_rotation + random.randint(-5, 5)

        self._outer_kite_height = random.randint(*height_range)
        self._outer_kite_width = random.randint(
            a=int(self._outer_kite_height / 3), b=self._outer_kite_height
        )

        self._outer_kite_diagonal_intersection_along_height = random.randint(2, 7) / 10
        self._inner_kite_diagonal_intersection_along_height = random.randint(4, 6) / 10

        self._outer_kite_offsets = (
            int(self._outer_kite_width / 4 + random.randint(-20, 20)),
            int(self._outer_kite_width / 10 + random.randint(-5, 5)),
            int(self._outer_kite_width / 10 + random.randint(-5, 5)),
            int(self._outer_kite_width / 4 + random.randint(-20, 20)),
        )

        self._outer_kite_line_width = min(1, int(5 / 300 * self._outer_kite_height))

        self._inner_kite_horizontal_offset = min(
            1, int(5 / 300 * self._outer_kite_height)
        )
        self._inner_kite_vertical_offset = min(1, int(5 / 200 * self._outer_kite_width))

        self._inner_kite_offset = random.randint(2, 6)

        self._inner_kite_height = random.randint(
            a=int(self._outer_kite_height / 10), b=int(self._outer_kite_height / 5)
        )
        self._inner_kite_width = random.randint(
            a=int(0.66 * self._inner_kite_height), b=int(2.25 * self._inner_kite_height)
        )

        self._limb_wdith = self._outer_kite_line_width + random.randint(a=0, b=3)

        self._right_arm_offset_from_center = random.randint(
            a=int(0.7 * self._outer_kite_width / 2),
            b=int(0.9 * self._outer_kite_width / 2),
        )
        self._right_arm_horizontal_distance = random.randint(
            a=1,
            b=15,
        )

        self._arm_start_height = random.randint(
            a=int(0.55 * self._outer_kite_height),
            b=int(0.7 * self._outer_kite_height),
        )
        self._arm_end_height = self._arm_start_height + random.randint(
            a=int(0.1 * self._outer_kite_height),
            b=int(0.35 * self._outer_kite_height),
        )

        self._left_arm_offset_from_center = random.randint(
            a=int(0.7 * self._outer_kite_width / 2),
            b=int(0.9 * self._outer_kite_width / 2),
        )
        self._left_arm_horizontal_distance = random.randint(
            a=1,
            b=15,
        )

        self._legs_offset_from_center = random.randint(
            a=int(0.1 * self._outer_kite_width / 2),
            b=int(0.2 * self._outer_kite_width / 2),
        )

        self._right_leg_horizontal_distance = random.randint(
            a=1,
            b=6,
        )

        self._left_leg_horizontal_distance = random.randint(
            a=1,
            b=6,
        )

        self._leg_start_height = 0.1 * self._outer_kite_height

        self._leg_end_height = -random.randint(
            a=int(0.3 * self._outer_kite_height),
            b=int(0.5 * self._outer_kite_height),
        )

        self._eyes_height = random.randint(
            a=int(0.7 * self._outer_kite_height),
            b=int(0.85 * self._outer_kite_height),
        )
        self._eyes_offset_from_center = random.randint(
            a=int(0.1 * self._outer_kite_width / 2),
            b=int(0.2 * self._outer_kite_width / 2),
        )

        eye_size = random.randint(
            a=self._outer_kite_line_width, b=2 * self._outer_kite_line_width
        )

        eye_sizes = [float(eye_size), float(eye_size)]

        different_sized_eye = random.choices(
            population=[0, 1, 2], weights=[0.1, 0.1, 0.8], k=1
        )[0]

        if different_sized_eye < 2:
            eye_sizes[different_sized_eye] *= random.uniform(a=0.75, b=1.3)

        self._eyes_sizes = tuple(eye_sizes)

    def create(self) -> PineCone:
        outer_kite = CurvedConvexKite(
            origin=self.origin,
            off_lines=(
                OffsetFromLine(offset=self._outer_kite_offsets[0]),
                OffsetFromLine(offset=self._outer_kite_offsets[1]),
                OffsetFromLine(offset=self._outer_kite_offsets[2]),
                OffsetFromLine(offset=self._outer_kite_offsets[3]),
            ),
            height=self._outer_kite_height,
            width=self._outer_kite_width,
            diagonal_intersection_along_height=self._outer_kite_diagonal_intersection_along_height,
            rotation=self._outer_kite_rotation,
        )

        inner_kite_factor = CurvedConvexKiteFactory(
            off_lines=(
                OffsetFromLine(offset=self._inner_kite_offset),
                OffsetFromLine(offset=-self._inner_kite_offset),
                OffsetFromLine(offset=-self._inner_kite_offset),
                OffsetFromLine(offset=self._inner_kite_offset),
            ),
            height=self._inner_kite_height,
            width=self._inner_kite_width,
            diagonal_intersection_along_height=self._inner_kite_diagonal_intersection_along_height,
            rotation=self._inner_kite_rotation,
            rotation_point=self.origin,
        )

        left_leg = Limb(
            start=rotate_about_point(
                Vec2D(-self._legs_offset_from_center, self._leg_start_height),
                self._outer_kite_rotation,
                self.origin,
            ),
            end=rotate_about_point(
                Vec2D(
                    -(
                        self._legs_offset_from_center
                        + self._left_leg_horizontal_distance
                    ),
                    self._leg_end_height,
                ),
                self._outer_kite_rotation,
                self.origin,
            ),
            off_line=OffsetFromLine(random.uniform(0.2, 0.8), -random.randint(3, 10)),
            size=self._limb_wdith,
        )

        right_leg = Limb(
            start=rotate_about_point(
                Vec2D(self._legs_offset_from_center, self._leg_start_height),
                self._outer_kite_rotation,
                self.origin,
            ),
            end=rotate_about_point(
                Vec2D(
                    self._legs_offset_from_center + self._right_leg_horizontal_distance,
                    self._leg_end_height,
                ),
                self._outer_kite_rotation,
                self.origin,
            ),
            off_line=OffsetFromLine(random.uniform(0.2, 0.8), -random.randint(3, 10)),
            size=self._limb_wdith,
        )

        eyes = Eyes(
            left_eye=rotate_about_point(
                Vec2D(-self._eyes_offset_from_center, self._eyes_height),
                self._outer_kite_rotation,
                self.origin,
            ),
            right_eye=rotate_about_point(
                Vec2D(self._eyes_offset_from_center, self._eyes_height),
                self._outer_kite_rotation,
                self.origin,
            ),
            left_eye_size=int(self._eyes_sizes[0]),
            right_eye_size=int(self._eyes_sizes[1]),
        )

        # mouth = RoundMouth(
        #    location=helpers.rotate_about_point(Vec2D(0, 180), rotation, s1), size=35
        # )

        mouth = CurvedMouth(
            start=rotate_about_point(
                Vec2D(-20, 180), self._outer_kite_rotation, self.origin
            ),
            end=rotate_about_point(
                Vec2D(20, 180), self._outer_kite_rotation, self.origin
            ),
            off_line=OffsetFromLine(0.8, -40),
            size=12,
        )

        left_arm = Limb(
            start=rotate_about_point(
                Vec2D(-self._right_arm_offset_from_center, self._arm_start_height),
                self._outer_kite_rotation,
                self.origin,
            ),
            end=rotate_about_point(
                Vec2D(
                    -(
                        self._right_arm_offset_from_center
                        + self._right_arm_horizontal_distance
                    ),
                    self._arm_end_height,
                ),
                self._outer_kite_rotation,
                self.origin,
            ),
            off_line=OffsetFromLine(random.uniform(0.2, 0.8), -random.randint(3, 10)),
            size=self._limb_wdith,
        )

        right_arm = Limb(
            start=rotate_about_point(
                Vec2D(-self._left_arm_offset_from_center, self._arm_start_height),
                self._outer_kite_rotation,
                self.origin,
            ),
            end=rotate_about_point(
                Vec2D(
                    -(
                        self._left_arm_offset_from_center
                        + self._left_arm_horizontal_distance
                    ),
                    self._arm_end_height,
                ),
                self._outer_kite_rotation,
                self.origin,
            ),
            off_line=OffsetFromLine(random.uniform(0.2, 0.8), random.randint(3, 10)),
            size=self._limb_wdith,
        )

        pine_cone = PineCone(
            outer_kite=outer_kite,
            inner_kite_factory=inner_kite_factor,
            outer_kite_line_width=self._outer_kite_line_width,
            horizontal_offset=self._inner_kite_horizontal_offset,
            vertical_offset=self._inner_kite_vertical_offset,
            initial_body_parts=(left_arm, right_arm),
            final_body_parts=(eyes, mouth, left_leg, right_leg),
        )

        return pine_cone
