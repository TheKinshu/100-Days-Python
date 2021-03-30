from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
atm = MoneyMachine()

coffeeMachine = True

while coffeeMachine:

    coffeeChoice = input("What would you like? (espresso/latte/cappuccino/): ")


    if coffeeChoice == 'report':
        machine.report()
        atm.report()
    elif coffeeChoice == 'off':
        coffeeMachine = False
    else:
        order = menu.find_drink(coffeeChoice)

        if not order == None:
            # Check Resource
            if machine.is_resource_sufficient(order):
                # Ask for coins
                # Check transaction
                if atm.make_payment(order.cost):
                    # Make coffee
                    machine.make_coffee(order)