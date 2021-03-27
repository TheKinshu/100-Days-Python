def decision(word):
    dec = input(word)
    return dec.lower()

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

while(True):
    choice = decision('You\'re at a cross road. Where do you want to go? Type "left" or right ')

    if choice == 'right':
        print("There it was a dead end, you inspect further but end up falling into a hole.\nGame Over.")
        break
    elif choice == 'left':
        choice = decision('You arrive at a river, the water current is very quick it will be hard to cross the river. What will you do? Type "swim" or "wait" ')
        
        if choice == 'swim':
            print("You try to swim across the river but the current was too fast, and you got swept away.\nGame Over.")
            break
        elif choice == 'wait':
            choice = decision('You decided to wait as the current is very fast and would have swept you away.\nYou spotted a in a distant coming towards you, the boat stopped right infront of you. What will you do? Type "aboard" "wait" "run" ')

            if not (choice == 'aboard'):
                print("Out of no-where tiger jumps out from the side and attacked you.\nGame Over.")
                break
            elif choice == 'aboard':
                print("You aboarded the ship, but there was no one. You look around to see if you can find anything worth taking. You approached a door and open it and found yourself treasure.\nYou win!")
                break
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload