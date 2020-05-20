import turtle
import math
import random


bob = turtle.Turtle()
bob.speed(30)
turtle.getscreen().bgcolor("black")
turtle.hideturtle()
colors = ["yellow", "red", "green", "blue", "orange", "violet", "indigo"]

for i in range(90):
    if i%2 == 0:
        bob.hideturtle()
        bob.circle(100)
        bob.color(random.choice(colors))
        bob.left(1)
    else:
        bob.hideturtle()
        bob.circle(-100)
        bob.color(random.choice(colors))
        bob.left(1)

turtle.done()
