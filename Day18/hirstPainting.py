import turtle as t
import random as r

tim = t.Turtle()
tim.speed('fastest')
t.colormode(255)
tim.penup()
color_list = [(254, 253, 250), (235, 246, 250), (251, 241, 246), (245, 252, 249), (243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31), (219, 129, 166), (161, 79, 35), (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81), (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7), (26, 165, 209), (16, 43, 132), (58, 166, 96), (134, 214, 229), (10, 101, 63), (133, 34, 20), (91, 27, 11), (159, 211, 188), (7, 90, 104), (252, 5, 63), (233, 172, 161), (105, 88, 9), (72, 129, 193), (178, 187, 217)]

tim.setheading(225)
tim.forward(350)
tim.setheading(0)

numberDot = 100

for a in range(1, numberDot+1):
    tim.dot(20, r.choice(color_list))
    tim.forward(50)
    if a % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Rules
# 10 x 10
# size = 20
# space = 50
screen = t.Screen()
screen.exitonclick()
