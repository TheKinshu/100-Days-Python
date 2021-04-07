from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

prefix_ypos = [-200, -150, -100, -50, 0 , 50, 100, 150, 200]

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.create_car()
        self.increaseSpeed = 0
    
        
    
    def create_car(self):
        for i in range(20):
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            self.restart(car)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT + self.increaseSpeed)

    def restart(self, car):
        chance = random.randint(0,4)
        if chance == 1:
            new_ypos = random.choice(prefix_ypos)

            car.goto((300,new_ypos))
        
    def checkPos(self):
        for i in range(len(self.cars)):
            if self.cars[i].xcor() < -300:
                self.restart(self.cars[i])

    def check_player_to_car(self, player):
        for i in range(len(self.cars)):
            if player.distance(self.cars[i]) < 25:
                return True
                
    def speedIncrease(self):
        self.increaseSpeed += 1


    
