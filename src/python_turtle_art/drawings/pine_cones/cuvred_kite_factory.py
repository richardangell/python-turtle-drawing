from turtle import Vec2D
from typing import Optional, Union

from ...lines.offset_from_line import OffsetFromLine
from ...polygons.kites.curved_kite import CurvedKite


class CurvedKiteFactory:
    """Factory allowing delay of CurvedKite creation with from_origin_and_dimensions.

    The arguments of CurvedKite.from_origin_and_dimensions can be speficied either in
    the initialisation of this class or later when the get_kite method is called.

    The rotation argument must be specified. When the CurvedKite object is created with
    get_kite it will be rotated by rotation degrees about the origin point.

    """

    def __init__(
        self,
        rotation: Union[int, float],
        origin: Optional[Vec2D] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        diagonal_intersection_along_height: Optional[float] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
    ):
        """Initialise the CurvedKiteFactory with optional args for CurvedKite."""
        self.rotation = rotation
        self.origin = origin
        self.height = height
        self.width = width
        self.diagonal_intersection_along_height = diagonal_intersection_along_height
        self.off_lines = off_lines

    def get_kite(
        self,
        origin: Optional[Vec2D] = None,
        height: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        diagonal_intersection_along_height: Optional[float] = None,
        off_lines: Optional[tuple[OffsetFromLine, ...]] = None,
    ) -> CurvedKite:
        """Return CurvedKite object and rotate about origin.

        If any of the arguments were not specified during initialisation of the
        CurvedKiteFactory object, they can be specified when get_kite is called. If
        however an argument is not specified during initialisation and also not
        specified when get_kite is called an exception will be raised.

        """

        if origin is None:
            if self.origin is None:
                raise ValueError("origin not specified")
            else:
                origin = self.origin

        if height is None:
            if self.height is None:
                raise ValueError("height not specified")
            else:
                height = self.height

        if width is None:
            if self.width is None:
                raise ValueError("width not specified")
            else:
                width = self.width

        if diagonal_intersection_along_height is None:
            if self.diagonal_intersection_along_height is None:
                raise ValueError("diagonal_intersection_along_height not specified")
            else:
                diagonal_intersection_along_height = (
                    self.diagonal_intersection_along_height
                )

        if off_lines is None:
            if self.off_lines is None:
                raise ValueError("off_lines not specified")
            else:
                off_lines = self.off_lines

        return CurvedKite.from_origin_and_dimensions(
            origin=origin,
            height=height,
            width=width,
            diagonal_intersection_along_height=diagonal_intersection_along_height,
            off_lines=off_lines,
        ).rotate(angle=self.rotation, about_point=origin)
