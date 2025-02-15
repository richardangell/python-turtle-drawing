from turtle import Vec2D

import pytest

from python_turtle_art.lines.line import Line


def test_jump_to_vertex_index():
    assert Line._jump_to_vertex_index == 0


def test_cannot_initiate_line_with_less_than_two_vertices():
    with pytest.raises(ValueError, match="vertices must contain at least 2 points."):
        Line(vertices=(Vec2D(0, 1),))
