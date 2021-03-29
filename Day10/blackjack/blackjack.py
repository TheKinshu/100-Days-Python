############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random, art, replit
from typing import ChainMap

# Add cards to the users hand from the deck
def hit(score, deck):
    position = random.randint(0, len(deck) - 1)
    card = deck[position]
    if deck[position] == 11 and score > 11:
        card = 1
        return card
    return card

# Dealing cards to players
def dealing(deck):
    hand = []
    score = 0
    for i in range(2):
        position = random.randint(0, len(deck) - 1)
        card = deck[position]
        if card == 11 and score > 11:
            card = 1
        hand.append(card)
        score += card
    
    return hand

def addScore(cards):
    score = 0
    for card in cards:
        score += card
    return score


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    playerHand = dealing(cards)
    computerHand = dealing(cards)
    computerScore = addScore(computerHand)

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    game_start = False

    # If user type 'y' then start the game, -
    # clear the screen, and print the blackjack logo.
    if start_game == 'y':
        replit.clear()
        game_start = True
        print(art.logo)

    while game_start:
        # Add up all the player scores
        playerScore = addScore(playerHand)
        print(f"\tYour cards: {playerHand}, current score: {playerScore}")
        print(f"\tComputer's first card: {computerHand[0]}")

        if playerScore > 21:
            print('You went over. You lose 😭')
            game_start = False
            game()
        
        if playerHand[0] + playerHand[1] == 21:
            print('You win, you got blackjack 😎')
            game()    

        decision = input("Type 'y' to get another card, type 'n' to pass: ")


        if computerHand[0] + computerHand[1] == 21:
            print('Dealer wins, they got blackjack 😨')
            game()

        #
        if decision == 'y':
            playerHand.append(hit(playerScore, cards))

        #
        else:
            game_start = False
            if computerScore < 17:
                computerHand.append(hit(computerHand, cards))
                if computerScore > 21:
                    print('Opponent went over. You win 😁')
                    game()
            
            #
            computerScore = addScore(computerHand)
            print(f"\tYour final hand: {playerHand}, final score {playerScore}")
            print(f"\tComputer's final hand: {computerHand}, final score {computerScore}")

            if playerScore > computerScore:
                print('You win 😃')
            elif playerScore == computerScore:
                print("It's a tie 😐")
            else:
                print('You lose 😤')

            # recursive
            game()

game()
    



