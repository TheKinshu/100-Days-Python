from turtle import Screen, Turtle, clearscreen, onclick, onkey
import random as re

s = Screen()
userBet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
s.setup(500,400)
colours = ['red', 'orange', 'wheat', 'green', 'blue', 'purple']

y = [-125, -75, -25, 25, 75, 125]

allTurtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(-230, y[turtle_index])
    allTurtle.append(new_turtle)

if userBet:
    is_race_on = True

while is_race_on:
    for turtle in allTurtle:
        randomeDis = re.randint(0, 10)
        turtle.forward(randomeDis)
        if turtle.xcor() > 205:
            is_race_on = False
            win = turtle.pencolor()
            if userBet == win:
                print(f"You've won! The {win} turtle won!")
                is_race_on = False
            else:
                print(f"You lose, the {win} turtle won.")
                is_race_on = False


s.exitonclick()
