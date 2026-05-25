from abc import ABC, abstractmethod
from turtle import RawTurtle

from ..polygons.convex_polygon import ConvexPolygon


class BaseConvexFill(ABC):
    """Base class for fillers.

    Subclasses of BaseFill can operate on convex and non-convex polygons.

    """

    @abstractmethod
    def fill(self, turtle: RawTurtle, polygon: ConvexPolygon):
        """Fill."""
        raise NotImplementedError
