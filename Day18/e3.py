#####Turtle Intro######

import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for i in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    
    timmy_the_turtle.pendown()


screen = t.Screen()
screen.exitonclick()