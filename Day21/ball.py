from turtle import Turtle, color



class Ball(Turtle):
    def __init__(self) -> None:
        self.xpos = 10
        self.ypos = 10
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.xpos
        new_y = self.ycor() + self.ypos
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ypos *= -1
    
    def bounce_x(self):
        self.xpos *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1