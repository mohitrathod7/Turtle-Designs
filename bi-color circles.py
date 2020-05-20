import turtle
import math
import random


bob = turtle.Turtle()
bob.speed(30)
turtle.getscreen().bgcolor("black")
turtle.hideturtle()

for i in range(100):
    if i%2 == 0:
        bob.hideturtle()
        bob.circle(100)
        bob.color("orange")
        bob.left(25)
    else:
        bob.hideturtle()
        bob.circle(-100)
        bob.color("green")
        bob.left(25)

turtle.done()
