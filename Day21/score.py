from turtle import Turtle

FONT = ('Courier', 80 , 'normal')
ALIGN = 'center'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.p1_score = 0
        self.p2_score = 0
        self.update_score()
        
        self.hideturtle()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.p1_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.p2_score, align=ALIGN, font=FONT)

    def point_p1(self):
        self.p1_score += 1
        self.clear()
        self.update_score()

    def point_p2(self):
        self.p2_score += 1
        self.clear()
        self.update_score()
