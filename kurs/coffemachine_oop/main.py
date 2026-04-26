from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

#choice = input("hello, what would you like to drink? (espresso/latte/cappuccino): ")

is_on = True

menu = Menu()
money_machine = MoneyMachine()
#money_machine.report()
coffee_maker = CoffeeMaker()
#coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"hello, what would you like to drink?: ({options}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)









