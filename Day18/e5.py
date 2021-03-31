import turtle as t
import random as r
tim = t.Turtle()
tim.shape("turtle")

colours = ['light sky blue', 'black', 'medium sea green', 'deep pink', 'medium spring green', 'slate blue', 'red', 'purple', 'SeaGreen', 'wheat']	

directions = [0, 90, 180, 270]

tim.pensize(5)
tim.speed('fastest')
for _ in range(200):
    tim.forward(30)
    tim.setheading(r.choice(directions))
    tim.color(r.choice(colours))

screen = t.Screen()
screen.exitonclick()
