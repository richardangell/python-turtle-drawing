from abc import ABC, abstractmethod
from turtle import Turtle


class BodyPart(ABC):
    @abstractmethod
    def draw(self, turtle: Turtle):
        raise NotImplementedError
