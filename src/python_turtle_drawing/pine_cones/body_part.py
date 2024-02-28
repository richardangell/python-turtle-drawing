from turtle import Turtle
from abc import ABC, abstractmethod


class BodyPart(ABC):
    @abstractmethod
    def draw(self, turtle: Turtle):
        raise NotImplementedError
