import turtle as t
import random as r
tim = t.Turtle()
tim.shape("turtle")

#colours = ['light sky blue', 'black', 'medium sea green', 'deep pink', 'medium spring green', 'slate blue', 'red', 'purple', 'SeaGreen', 'wheat']	

directions = [0, 90, 180, 270]
t.colormode(255)

def randomColour():
    re = r.randint(0, 255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    myTuple = (re, g, b)
    return myTuple

tim.pensize(5)
tim.speed('fastest')

for _ in range(200):
    tim.forward(30)
    tim.setheading(r.choice(directions))
    tim.color(randomColour())

screen = t.Screen()
screen.exitonclick()
