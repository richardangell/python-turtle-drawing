from turtle import Turtle, Vec2D
import turtle as t
from typing import Union
from math import pi, cos, sin


def jump_to(turtle: Turtle, position: Vec2D) -> None:
    """Move turtle to position without drawing line to position."""
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()


def turn_off_turtle_animation():
    """Turn off turtle animation."""
    t.tracer(0, 0)


def update_screen():
    """Update screen (after turning off turtle animation.)"""
    t.update()


def convert_degrees_to_radians(degrees: Union[int, float]) -> float:
    """Convert an angle in degress to radians."""
    return degrees * pi / 180


def rotate_about_point(
    point: Vec2D, angle: Union[int, float], rotate_about_point: Vec2D = Vec2D(0, 0)
) -> Vec2D:
    """Rotate point through angle (in degrees) about another point.

    References:
        https://math.stackexchange.com/a/4434146

    """

    angle_radians = convert_degrees_to_radians(angle)

    x_minus_alpha = point[0] - rotate_about_point[0]
    y_minus_beta = point[1] - rotate_about_point[1]

    rotated_x = (
        rotate_about_point[0]
        + x_minus_alpha * cos(angle_radians)
        - y_minus_beta * sin(angle_radians)
    )

    rotated_y = (
        rotate_about_point[0]
        + x_minus_alpha * sin(angle_radians)
        + y_minus_beta * cos(angle_radians)
    )

    return Vec2D(rotated_x, rotated_y)
