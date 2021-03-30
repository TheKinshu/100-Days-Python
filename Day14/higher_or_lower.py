import art, game_data, random, replit

logo = art.logo
gameData = game_data.data
vs = art.vs

def pickCelebrity(data, person = ''):
    pick = random.randint(0, len(data) - 1)
    if person == data[pick]['name']:
        pick = random.randint(0, len(data) - 1)
    return data[pick]

def checkFollowers(guess, follower1, follower2):
    if guess == 'A' or guess == 'a':
        if follower1 > follower2:
            return True
        else:
            return False
    if guess == 'B' or guess == 'b':
        if follower1 < follower2:
            return True
        else:
            return False



def game():
    score = 0

    first = pickCelebrity(gameData)
    second = pickCelebrity(gameData, first['name'])
    game_continue = True

    replit.clear()
    
    while game_continue:
        print(logo)
        
        # Print out score
        if score > 0:
            print(f"You're roght! Current score: {score}")

        print(f"Compare A: {first['name']}, {first['description']}, from {first['country']}")
        print(vs)
        print(f"Compare B: {second['name']}, {second['description']}, from {second['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ")

        result = checkFollowers(guess, first['follower_count'], second['follower_count'])
        if result:
            score += 1
            first = second
            second = pickCelebrity(gameData, first['name'])
            replit.clear()
        else:
            game_continue = False
            replit.clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

game()