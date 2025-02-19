from turtle import Vec2D


def get_horizontal_intersection_of_line(
    p0: Vec2D, p1: Vec2D, constant: int | float
) -> Vec2D:
    """Get the point at which a line intersects a horizontal line.

    Args:
        p0 (Vec2D): The first point defining the line.
        p1 (Vec2D): The second point defining the line.
        constant (int): The y-coordinate of the horizontal line.

    """
    p0_to_p1 = p1 - p0

    p0_to_y = constant - p0[1]

    try:
        t = p0_to_y / p0_to_p1[1]
    except ZeroDivisionError as err:
        raise ValueError("Line p0, p1 is horizontal.") from err

    intersection = p0 + (p0_to_p1 * t)

    return intersection


def get_vertical_intersection_of_line(
    p0: Vec2D, p1: Vec2D, constant: int | float
) -> Vec2D:
    """Get the point at which a line intersects a vertical line.

    Args:
        p0 (Vec2D): The first point defining the line.
        p1 (Vec2D): The second point defining the line.
        constant (int): The y-coordinate of the vertical line.

    """
    p0_to_p1 = p1 - p0

    p0_to_x = constant - p0[0]

    try:
        t = p0_to_x / p0_to_p1[0]
    except ZeroDivisionError as err:
        raise ValueError("Line p0, p1 is vertical.") from err

    intersection = p0 + (p0_to_p1 * t)

    return intersection
