from turtle import RawTurtle, TurtleScreen, Vec2D


def jump_to(turtle: RawTurtle, position: Vec2D) -> None:
    """Move turtle to position without drawing line to position."""
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()


def turn_off_turtle_animation(screen: TurtleScreen):
    """Turn off turtle animation."""
    screen.tracer(0, 0)


def update_screen(screen: TurtleScreen):
    """Update screen (after turning off turtle animation.)"""
    screen.update()
