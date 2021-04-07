from os import stat
from turtle import Turtle as t, update
import pandas

class States(t):
    
    def __init__(self) -> None:
        super().__init__()
        self.path = './Day25/us_states.csv'
        self.data = self.create_states(self.path)
        self.states = self.get_states(self.data)
        self.position = self.get_position(self.data)
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.goto(1000,1000)

        self.score = 0

    def create_states(self, pathURL):
        return pandas.read_csv(pathURL)
    
    def get_states(self, data):
        return data['state'].to_list()
    
    def get_position(self, data):
        pos_list = []
        xpos = data['x'].to_list()
        ypos = data['y'].to_list()

        for i in range(len(xpos)):
            pos = [xpos[i], ypos[i]]
            pos_list.append(pos)

        return pos_list
    
    def update_map(self, index):
        xpos = self.position[index][0]
        ypos = self.position[index][1]

        self.goto(xpos, ypos)
        self.write(f"{self.states[index]}")


    def guess_state(self, guess):
        indexNum = 0
        guess = guess.title()
        if guess in self.states:
            indexNum = self.states.index(guess)
            self.update_map(indexNum)
            self.score += 1

            return True

    def continue_game(self):
        if self.score == len(self.states):
            return False

        else:
            return True

    def final_score(self, data):
        not_guessed = [state for state in self.states if state not in data]

        #for state in self.states:
        #    if state not in data:
        #        not_guessed.append(state)

        #print(not_guessed)

        df = pandas.DataFrame(not_guessed)
        
        df.to_csv("./Day25/missing_states.csv")