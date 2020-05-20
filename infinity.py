import turtle
import math


a = 200
b = 100

pop = turtle.Turtle()
pop.hideturtle()
pop.speed(5)


for i in range(33):
    if i == 0:
        pop.up()
    else:
        pop.down()
                
    pop.setposition(a*math.cos(i/10), b*math.sin(i/5))
    pop.setposition(a*math.cos(i/10), b*math.sin(i/-5))


turtle.done()
