# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

score1 = 0
score2 = 0

true = 'true'
love = 'love'

for i in range(len(true)):
    score1 += (name1.count(true[i]) + name2.count(true[i]))
    score2 += (name1.count(love[i]) + name2.count(love[i]))

loveScore = int(str(score1) + str(score2))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")