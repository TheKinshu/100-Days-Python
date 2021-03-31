import turtle as t
import random as r
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")

colours = ['light sky blue', 'black', 'medium sea green', 'deep pink', 'medium spring green', 'slate blue', 'red', 'purple', 'SeaGreen', 'wheat']	

def drawShape(sides):
    angle = 360/ sides

    for i in range(sides):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.right(angle)

for shp in range(3,50):
    timmy_the_turtle.color(r.choice(colours))
    drawShape(shp)

screen = t.Screen()
screen.exitonclick()
