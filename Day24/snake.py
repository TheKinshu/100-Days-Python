from turtle import Turtle, forward, up

STARTING_POS = [(0,0), (-20, 0), (-40, 0)]
# Speed
MOVE_DIS = 20
# Controls
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self) -> None:

        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for i in STARTING_POS:
            self.add_part(i)

    def add_part(self, position):
            body = Turtle('square')
            body.penup()
            body.color('white')
            body.goto(position)
            self.snake.append(body)
    
    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_part(self.snake[-1].position())

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            xpos = self.snake[i - 1].xcor()
            ypos = self.snake[i - 1].ycor()
            self.snake[i].goto(xpos,ypos)

        self.snake[0].forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)