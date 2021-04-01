from food import Food
from snake import Snake
from score_board import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game = True

while game:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    # Detecting collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add()
        snake.extend()
    # Dectect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        scoreboard.game_over()

    # Dectecting collision with snake body
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            game = False
            scoreboard.game_over()










screen.exitonclick()