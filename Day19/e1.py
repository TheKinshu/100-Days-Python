from turtle import Screen, Turtle, clearscreen, onclick, onkey

t = Turtle()
ts = Turtle()
s = Screen()

def move_foward():
    t.forward(10)

def move_backward():
    t.back(10)

def clockwise():
    newHead = t.heading() - 10
    t.setheading(newHead)

def anticlock():
    newHead = t.heading() + 10
    t.setheading(newHead)

def clearsscreen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(key='w', fun=move_foward)
s.onkey(key='s', fun=move_backward)
s.onkey(key='d', fun=clockwise)
s.onkey(key='a', fun=anticlock)
s.onkey(key='c', fun=clearsscreen)

s.exitonclick()
