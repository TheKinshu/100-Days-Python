# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
'''
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''
total = round((weight / height **2), 0)

if total < 18.5:
    print(f"Your BMI is {total}, you are underweight.")
elif total < 25:
    print(f"Your BMI is {total}, you are normal weight.")
elif total < 30:
    print(f"Your BMI is {total}, you are slightly overweight.")
elif total < 35:
    print(f"Your BMI is {total}, you are obese.")
else:
    print(f"Your BMI is {total}, you are clinically obese.")
