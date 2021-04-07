import art, random

def checkGuess(guessNum, answerNum):
    if guessNum > answerNum:
        return "Too high."
    elif guessNum < answerNum:
        return "Too low."
    elif guessNum == answerNum:
        return "Correct"

def loseLive(live):
    if live > 1:
        return live - 1
    else:
        return "Game Over"
def guessNumber():
    print(art.logo)

    print("Welcome to Guess The Number!")
    print("Your objective is to guess what number Im thinking.")
    print("I'm thinking of a number between 1 and 100")

    # TODO Generate a number
    answer = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    lives = 0

    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 6

    game = True

    # TODO: loop through until either guess is completed or lives are depleted
    while game:
        print(f"You have {lives} attempts remaining to guess the number.")

        # TODO: Ask player to guess
        guess = int(input("Make a guess: "))

        check = checkGuess(guess, answer)

        if check == 'Correct':
            print(f"You got it! The answer was {answer}")
            game = False
        else:
            print(check)
            lives = loseLive(lives)
            if lives == "Game Over":
                print("You've run out of guesses, you lose.")
                game = False

guessNumber()