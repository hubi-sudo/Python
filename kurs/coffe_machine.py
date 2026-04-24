menu = {
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
    },
}

resources = {"water": 300,
             "milk": 200,
             "coffe": 100
             }

profit = 0


def check_resources(wybor):
    global profit
    if 'milk' in menu[wybor]['ingredients']:
        if menu[wybor]['ingredients']['water'] < resources['water']:
            if menu[wybor]['ingredients']['coffee'] < resources['coffe']:
                if menu[wybor]['ingredients']['milk'] < resources['milk']:
                    return True
                else:
                    print("Not enough milk")
                    return False
            else:
                print("Not enough coffee")
                return False
        else:
            print("Not enough water")
            return False
    else:
        if menu[choice]['ingredients']['water'] < resources['water']:
            if menu[choice]['ingredients']['coffee'] < resources['coffe']:
                return True
            else:
                print("Not enough coffee")
                return False
        else:
            print("Not enough water")
            return False

def check_money(kafka):
    global total
    total = 0
    print("Please insert coins.")
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    if total > menu[kafka]['cost']:
        change = round(total - menu[kafka]['cost'],2)
        print(f"You have ${change} of change")
        return True
    else:
        print("You have not enough money")
        return False


def make_coffe(kawa):
    if 'milk' in menu[kawa]['ingredients']:
        resources['water'] -= menu[kawa]['ingredients']['water']
        resources['coffe'] -= menu[kawa]['ingredients']['coffee']
        resources['milk'] -= menu[kawa]['ingredients']['milk']
        profit += menu[choice]['cost']
    else:
        resources['water'] -= menu[kawa]['ingredients']['water']
        resources['coffe'] -= menu[kawa]['ingredients']['coffee']
        profit += menu[choice]['cost']



trueOrFalse = True
while trueOrFalse:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        trueOrFalse = False
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffe']}\nMoney: {profit}")
    elif choice != "espresso" and choice != "latte" and choice != "cappuccino":
        print("There's no such thing, try again.")
    else:
        if check_resources(choice):
            if check_money(choice):
                make_coffe(choice)
                print(f"Enjoy your {choice}!")



