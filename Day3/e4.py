# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
subTotal = 0

# Choose topping
if size == 'S':
    subTotal = 15
elif size == 'M':
    subTotal = 20
elif size == 'L':
    subTotal = 25

if size == 'S' and add_pepperoni == 'Y':
    subTotal += 2
elif add_pepperoni == 'Y':
    subTotal += 3

if extra_cheese == 'Y':
    subTotal += 1

print(f"Your final bill is: ${subTotal}.")