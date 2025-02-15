from abc import ABC, abstractmethod
from turtle import Turtle


class BaseFill(ABC):
    @abstractmethod
    def pre_draw(self, turtle: Turtle):
        """Pre edge-drawing step."""
        raise NotImplementedError

    @abstractmethod
    def post_draw(self, turtle: Turtle):
        """Post edge-drawing step."""
        raise NotImplementedError
