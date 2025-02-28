from turtle import RawTurtle, Vec2D

from python_turtle_art.filling import ColourFill
from python_turtle_art.lines import Line
from python_turtle_art.polygons.kites.convex_kite import ConvexKite


def draw_image(turtle: RawTurtle):
    l = 50
    u = 50

    kite = ConvexKite(vertices=(Vec2D(-l, -l), Vec2D(u, -l), Vec2D(u, u), Vec2D(-l, u)))
    kite.draw(turtle, size=0.5)
    kite.fill(turtle, ColourFill("yellow"))

    # Line(vertices=()).draw(turtle, size=0.5)
    # Line(vertices=(Vec2D(u, -l), Vec2D(u, u))).draw(turtle, size=0.5)
    # Line(vertices=(Vec2D(u, u), Vec2D(-l, u))).draw(turtle, size=0.5)
    # Line(vertices=(Vec2D(-l, u), Vec2D(-l, -l))).draw(turtle, size=0.5)

    # bottom left
    l = -49
    u = -2
    kite = ConvexKite(vertices=(Vec2D(l, l), Vec2D(u, l), Vec2D(u, u), Vec2D(l, u)))
    kite.draw(turtle, size=0.5, colour="grey")

    # top right
    l = 49
    u = 2
    kite = ConvexKite(vertices=(Vec2D(l, l), Vec2D(u, l), Vec2D(u, u), Vec2D(l, u)))
    kite.draw(turtle, size=0.5, colour="grey")

    # bottom right
    l = -49
    u = -2
    kite = ConvexKite(vertices=(Vec2D(-l, l), Vec2D(-l, u), Vec2D(-u, u), Vec2D(-u, l)))
    kite.draw(turtle, size=0.5, colour="grey")

    # top left
    l = -49
    u = -2
    kite = ConvexKite(vertices=(Vec2D(l, -l), Vec2D(l, -u), Vec2D(u, -u), Vec2D(u, -l)))
    kite.draw(turtle, size=0.5, colour="grey")

    yellow_fill = ColourFill("yellow")
    # kite.fill(turtle, yellow_fill)
    # kite.draw(turtle, size=1)

    # turtle.penup()
    # turtle.goto(0, 0)
    # turtle.pendown()
    # turtle.dot(size=1)

    # Line(vertices=(Vec2D(-100, 0), Vec2D(100, 0))).draw(turtle, size=1)
    # Line(vertices=(Vec2D( 0, 100), Vec2D(0, -100))).draw(turtle, size=1)

    Line(vertices=(Vec2D(-40, -30), Vec2D(20, 45))).draw(turtle, size=0.5)
    # Line(vertices=(Vec2D(-100, 100), Vec2D(100, -100))).draw(turtle, size=0.5)

    # time.sleep(10)
