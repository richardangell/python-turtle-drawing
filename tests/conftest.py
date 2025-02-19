from turtle import Turtle

import pytest


class MockedTurtle(Turtle):
    """Dummy class inheriting from Turtle but not doing anything on initialisation."""

    def __init__(self):
        pass


@pytest.fixture(scope="session")
def mocked_turtle() -> MockedTurtle:
    return MockedTurtle()
