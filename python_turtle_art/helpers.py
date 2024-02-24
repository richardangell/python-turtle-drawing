from turtle import Turtle, Vec2D
import turtle as t


def jump_to(turtle: Turtle, position: Vec2D) -> None:
    """Move turtle to position without drawing line to position."""
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()


def turn_off_turtle_animation():
    """Turn off turtle animation."""
    t.tracer(0, 0)


def update_screen():
    """Update screen (after turning off turtle animation.)"""
    t.update()
