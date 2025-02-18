from turtle import Vec2D


def get_horizontal_intersection_of_line(
    p0: Vec2D, p1: Vec2D, horizontal_y: int
) -> Vec2D:
    """Get the point at which a line intersects a horizontal line.

    Args:
        p0 (Vec2D): The first point defining the line.
        p1 (Vec2D): The second point defining the line.
        horizontal_y (int): The y-coordinate of the horizontal line.

    """
    p0_to_p1 = p1 - p0

    p0_to_y = horizontal_y - p0[1]

    t = p0_to_y / p0_to_p1[1]

    intersection = p0 + (p0_to_p1 * t)

    return intersection
