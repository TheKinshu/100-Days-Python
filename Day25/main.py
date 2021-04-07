from os import stat
import turtle

from state import States

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
state = States()

image = "./Day25/blank_states_img.gif"

state_guessed = []

screen.addshape(image)

turtle.shape(image)


titleGame = "Guess the State"

game = True
while game:
    answer = screen.textinput(title= titleGame, prompt="What's another state's name?")

    if not answer == 'exit':
        if state.guess_state(answer):
            state_guessed.append(answer.title())
        game = state.continue_game()
        titleGame = f"{state.score}/50 States Correct"
    else:
        game = False
    
state.final_score(state_guessed)
