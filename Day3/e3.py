# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# On every year that is evenly divisible by 4 is a leap year
# but every year that is evenly divisble by 100 is not a leep year
# unless the year is also evenly divisble by 400 then its a leap year

leapYear = False

if year % 4 == 0:
    leapYear = True
    if year % 100 == 0:
        leapYear = False
        if year % 400 == 0:
            leapYear = True          

if leapYear:
    print("Leap Year")
else:
    print("Not leep year")
