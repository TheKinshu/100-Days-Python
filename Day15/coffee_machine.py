MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def getWallet(quarter, dime, nickle, penny):
    total = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
    return total

def checkResources(resource, choice):
    for res in resource:
        if not (choice == 'espresso' and res == 'milk'):
            check1 = resource[res]
            check2 = MENU[choice]['ingredients'][res]
            if check1 < check2:
                print(f"Sorry there is not enough {res}")
                coffeeMachine()
    return True

def useResources(resource, choice):
    for res in resource:
        if not (choice == 'espresso' and res == 'milk'):
            resource[res] -= MENU[choice]['ingredients'][res]
    return resource

def coffeeMachine():

    currentResource = resources

    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    
    if coffee == 'report':
        print(f"Water: {currentResource['water']}ml\nMilk: {currentResource['milk']}ml\nCoffe: {currentResource['coffee']}g")
        coffeeMachine()

    checkResources(currentResource, coffee)

    print("Please insert coins.")

    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    wallet = getWallet(quarters, dimes, nickles, pennies)

    balance = round(wallet - MENU[coffee]['cost'], 2)
    if balance < 0:
        print("Sorry that's not enough money. Money refunded.")
        coffeeMachine()
    else:
        print(f"Here is ${balance} in change.")
        print(f"Here is your {coffee} ☕ Enjoy!")
        currentResource = useResources(currentResource, coffee)
        coffeeMachine()


coffeeMachine()
