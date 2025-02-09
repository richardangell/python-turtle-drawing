from math import pi
from typing import Union


def convert_degrees_to_radians(degrees: Union[int, float]) -> float:
    """Convert an angle in degress to radians."""
    return degrees * pi / 180


def convert_clockwise_angle_to_counter_clockwise(
    degrees: Union[int, float],
) -> Union[int, float]:
    """Convert clockwise positive angle to counter clockwise positive."""
    return 360 - (degrees % 360)
