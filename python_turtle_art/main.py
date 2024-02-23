from turtle import Screen, Turtle, Vec2D

from line import draw_curved_line, OffsetFromLine


if __name__ == "__main__":
    turtle = Turtle()

    s1 = Vec2D(0, 0)
    s2 = Vec2D(-100, 100)
    s3 = Vec2D(0, 200)
    s4 = Vec2D(100, 100)
    s5 = Vec2D(0, 0)

    turtle.begin_fill()

    draw_curved_line(s1, s2, OffsetFromLine(offset=-20), steps=20)
    draw_curved_line(s2, s3, OffsetFromLine(offset=20), steps=20)
    draw_curved_line(s3, s4, OffsetFromLine(offset=20), steps=20)
    draw_curved_line(s4, s1, OffsetFromLine(offset=-20), steps=20)

    turtle.end_fill()

    screen = Screen()
    screen.exitonclick()
