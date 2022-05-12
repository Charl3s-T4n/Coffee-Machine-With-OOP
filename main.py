from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()       # Create new instance of the object money_machine
coffee_maker = CoffeeMaker()         # Create new instance of the object coffee_maker
menu = Menu()                        # Create menu object from Menu Class

is_on = True   # Create flag variable
#money_machine.report()    # call the method report that belongs to class MoneyMachine: shows the $
#coffee_maker.report()     # call the method report: which prints a report of all the resources

while is_on:   # while True
    options = menu.get_items()     # Returns names of available menu items
    choice = input(f"What would you like? ({options}): ")  # Shows user what drinks available
    if choice == "off":                     # when user key in 'off'
        is_on = False   # Ends while loop
    elif choice == "report":                # when user key in 'report'
        coffee_maker.report()     # Shows report of all ingredients
        money_machine.report()    # Shows report of $
    else:
        drink = menu.find_drink(choice)   # find if the drink user input is available
        if coffee_maker.is_resource_sufficient(drink):    # Returns True if enough ingredients currently, False otherwise
            if money_machine.make_payment(drink.cost): # Returns True if enough $ inserted, False if otherwise
                coffee_maker.make_coffee(drink)      # deducts required ingredients from resources if enough $ inserted


