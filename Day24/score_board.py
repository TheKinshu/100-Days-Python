from turtle import Turtle
import turtle

FONT = ('Courier', 20 , 'normal')
ALIGN = 'center'

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highScore = self.getHighScore()
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    
    def getHighScore(self):
        with open('./Day24/data.txt') as file:
            return int(file.read())

    def save_Score(self):
        with open('./Day24/data.txt', mode='w') as file:
            file.write(f"{self.highScore}")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore} ", False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            self.save_Score()
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", False, align=ALIGN, font=FONT)

    def add(self):
        self.score += 1
        self.update_score()
        