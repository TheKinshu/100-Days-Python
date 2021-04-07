from score import Score
from turtle import Screen
from paddle import Paddle
from ball import Ball

import time

# Setting up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

score = Score()

player2 = Paddle((350, 0))

player1 = Paddle((-350,0))

ball = Ball()



screen.listen()

screen.onkey(player2.go_up, 'Up')
screen.onkey(player2.go_down, 'Down')

screen.onkey(player1.go_up, 'w')
screen.onkey(player1.go_down, 's')


game = True


while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        score.point_p1()

    if ball.xcor() < -380:
        ball.restart()
        score.point_p2()

# Close on click
screen.exitonclick()