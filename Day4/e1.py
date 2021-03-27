#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

predict = input('Guess what the coin is? "Heads" or "Tails" ')

coin = random.randint(0,1)

if coin == 1:
    print("It's Heads")
    coinSide = 'heads'
else:
    print("It's Tails")
    coinSide = 'tails'

if predict.lower() == coinSide:
    print('You win!')
else:
    print('You lose.')