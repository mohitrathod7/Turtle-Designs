import turtle
import math


a = 100
b = 110

pop = turtle.Turtle()
pop.hideturtle()
pop.speed(5)


for i in range(8):
    pop.goto(0,0)
    pop.forward(a*math.cos(i/5))
    pop.left(45)
    pop.forward(b*math.sin(i/5))
    pop.dot(1)

pop.left(90)
pop.forward(12)
pop.left(90)
pop.forward(20)

turtle.done()
