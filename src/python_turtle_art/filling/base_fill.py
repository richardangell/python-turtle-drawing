from abc import ABC, abstractmethod
from turtle import Turtle, Vec2D


class BaseFill(ABC):
    @abstractmethod
    def fill(self, turtle: Turtle, vertices: tuple[Vec2D, ...]):
        """Fill."""
        raise NotImplementedError
