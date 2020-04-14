import turtle


def draw_this():
    """Makes a turtle draw 5 squares inside of each other"""

    bob = turtle.Turtle()
    window = turtle.Screen()
    for i in range(4):
        bob.up()
        bob.ht()
        bob.goto(-i * 10, -i * 10)
        bob.st()
        bob.down()
        for j in range(4):
            bob.forward(20 * (i + 1))
            bob.left(90)
    turtle.Screen().mainloop()


def test_draw_this():
    """Test if the function is working"""
    draw_this()


test_draw_this()
