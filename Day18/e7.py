import turtle as t
import random as r
tim = t.Turtle()
tim.shape("turtle")

t.colormode(255)

def randomColour():
    re = r.randint(0, 255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    myTuple = (re, g, b)
    return myTuple

tim.speed('fastest')
def draw_spir(size):
    for _ in range(int(360/ size)):
        tim.color(randomColour())
        tim.circle(50)
        tim.setheading(tim.heading() + size)

draw_spir(1)


screen = t.Screen()
screen.exitonclick()
