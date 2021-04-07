import time
from turtle import Screen, setpos
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

carmanager = CarManager()

score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.move()
    carmanager.checkPos()

    if carmanager.check_player_to_car(player):
        game_is_on = False
        score.game_over()

    if player.ycor() > 280:
        carmanager.speedIncrease()
        score.add_score()
        player.restart()


screen.exitonclick()

