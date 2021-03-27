#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# https://www.w3schools.com/python/ref_random_shuffle.asp

password_length = nr_letters + nr_numbers + nr_symbols

password = []

letterCount = 0
numberCount = 0
symbolCount = 0


while not (len(password) == password_length):

    radomised = random.randint(0,2)

    if radomised == 1:
        if not (letterCount == nr_letters):
            x = random.randint(0,len(letters)-1)
            password +=(letters[x])

    elif radomised == 2:
        if not (numberCount == nr_numbers):
            x = random.randint(0,len(numbers)-1)
            password += (numbers[x])

    else:
        if not (symbolCount == nr_symbols):
            x = random.randint(0,len(symbols)-1)
            password += (symbols[x])

print(password)