import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

result = 0

choices = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

computerChoices = random.randint(0,2)

action1 = ['Tie', 'You Lose', 'You win']
action2 = ['You win', 'Tie', 'You Lose']
action3 = ['You Lose', 'You win', 'Tie']

action =  [action1, action2, action3]

print('Player:')
if choices == 0:
    print(rock)
elif choices == 1:
    print(paper)
elif choices == 2:
    print(scissors)

print('Computer:')
if computerChoices == 0:
    print(rock)
elif computerChoices == 1:
    print(paper)
elif computerChoices == 2:
    print(scissors)

result = action[choices][computerChoices]

print(result)
