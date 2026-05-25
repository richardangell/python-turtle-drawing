"""Top level conftest.py.

This conftest adds a custom command line argument --disable-beartype used in
combination with the pytest_configure hook function implementation to
disable beartype by initialising it with BeartypeStrategy.O0 strategy in the
package's top level __init__.py file.

For this to work no conftest.py files can import from the package at the top
of the script (as is usual) otherwise the package is imported before the
environment variable is set.

"""

import os
from turtle import Turtle

import pytest


def pytest_addoption(parser: pytest.Parser):
    """Add custom --disable-beartype command line argument.

    This will be used to set the DISABLE_BEARTYPE environment variable before the
    package is imported - so that beartype can be disabled.

    """
    parser.addoption("--disable-beartype", action="store_true")


def pytest_configure(config: pytest.Config):
    """Set the DISABLE_BEARTYPE enrivonment variable if --disable-beartype passed.

    As long as this is executed before the package is imported then beartype will
    be configured with strategy BeartypeStrategy.O0 i.e. disabled. See
    src/python_turtle_art/__init__.py for details.

    """
    if config.getoption("--disable-beartype"):
        os.environ["DISABLE_BEARTYPE"] = "1"


class MockedTurtle(Turtle):
    """Dummy class inheriting from Turtle but not doing anything on initialisation."""

    def __init__(self):
        pass


@pytest.fixture(scope="session")
def mocked_turtle() -> MockedTurtle:
    """Return mocked Turtle object that does nothing on initialisation."""
    return MockedTurtle()
