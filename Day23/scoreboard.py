from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        
        self.playerLevel = 1
        self.update_score()

    def update_score(self):
        self.goto(-200, 250)
        self.write(f"Level: {self.playerLevel}", align=ALIGN, font=FONT)
    
    def add_score(self):
        self.playerLevel += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGN, font=FONT)
