from turtle import Turtle, Vec2D


def jump_to(turtle: Turtle, position: Vec2D) -> None:
    """Move turtle to position without drawing line to position."""
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
