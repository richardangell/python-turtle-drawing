from abc import ABC, abstractmethod
from turtle import RawTurtle

from ..polygons.polygon import Polygon


class BaseFill(ABC):
    """Base class for fillers.

    Subclasses of BaseFill can operate on convex and non-convex polygons.

    """

    @abstractmethod
    def fill(self, turtle: RawTurtle, polygon: Polygon):
        """Fill."""
        raise NotImplementedError
