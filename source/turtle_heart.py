""""
This code uses the built-in turtle library
and results in drawing a heart with "devpythonbr"
written in the center of the heart

-> Requirements:
    . pip install Pillow
"""

import turtle

t = turtle.Turtle()

t.hideturtle()
t.goto(0, -10)
t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(178)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-120, 130)
t.pendown()
t.color('white')
t.write("DevPythonBr", font=("Roboto", 25, "bold"))

turtle.done()
