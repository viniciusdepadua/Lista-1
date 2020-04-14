import turtle
import time


def draw_poly(t, n, sz):
    """makes a turtle 't' draw a regular
polygon with size sz and n sides."""

    s_intern_angles = (n - 2) * 180
    for i in range(n):
        t.forward(sz)
        t.left(180 - s_intern_angles / n)
    time.sleep(5)
    turtle.Screen().clear()


def test_draw_poly():
    """Test draw_poly drawing poligons from triangle to a eneagon"""

    for i in range(7):
        bob = turtle.Turtle()
        draw_poly(bob, i + 3, 100)


test_draw_poly()
