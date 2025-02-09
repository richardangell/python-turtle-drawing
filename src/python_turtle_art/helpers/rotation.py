from math import cos, sin
from turtle import Vec2D
from typing import Union

from .angles import (
    convert_clockwise_angle_to_counter_clockwise,
    convert_degrees_to_radians,
)


def rotate_about_point(
    point: Vec2D, angle: Union[int, float], rotate_about_point: Vec2D | None = None
) -> Vec2D:
    """Rotate point through angle (in degrees) about another point.

    Note, formula is for counterclockwise rotation being positive so
    angle is reversed before calculating.

    References:
        https://math.stackexchange.com/a/4434146

    """
    rotate_about_point_ = (
        Vec2D(0, 0) if rotate_about_point is None else rotate_about_point
    )

    if point == rotate_about_point_:
        return point

    else:
        angle_reversed = convert_clockwise_angle_to_counter_clockwise(angle)
        angle_radians = convert_degrees_to_radians(angle_reversed)

        x_minus_alpha = point[0] - rotate_about_point_[0]
        y_minus_beta = point[1] - rotate_about_point_[1]

        rotated_x = (
            rotate_about_point_[0]
            + x_minus_alpha * cos(angle_radians)
            - y_minus_beta * sin(angle_radians)
        )

        rotated_y = (
            rotate_about_point_[1]
            + x_minus_alpha * sin(angle_radians)
            + y_minus_beta * cos(angle_radians)
        )

        return Vec2D(rotated_x, rotated_y)
