from turtle import Turtle
import turtle

FONT = ('Courier', 20 , 'normal')
ALIGN = 'center'

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT)

    def add(self):
        self.score += 1
        self.update_score()
        