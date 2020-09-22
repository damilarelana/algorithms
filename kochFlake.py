import turtle
t = turtle.Turtle()

"""
    We create kochLine fractal first
    Then we duplicate the line fractal to 3 sides of a triangle
    "fractal lines" on 3 sides of a triangle, gives you the "fractal flake"

    Steps:
        - draw a line       [handled by "kochLine" recursive function]
        - rotate to the right by 120 degrees
"""


def kochLine(order, size):
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        for n in [60, -120, 60, 0]:
            kochLine((order - 1), (size/3))  # Go 1/3 of the way
            t.left(n)

def kochFlake(order, size):
        for n in range(0, 3):
            kochLine(order, size)   # Go 1/3 of the way
            t.right(120)

kochFlake(4, 240)
input()