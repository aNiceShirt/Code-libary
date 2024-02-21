from numpy import round

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

machine_on = True

def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print("The coffee machine currently contains:")
    print(f"Water = {water} ml")
    print(f"Milk = {milk} ml")
    print(f"Coffee = {coffee} g")


def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    report()


def payment(drink_cost):
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))
    total_amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    total_change = 0
    if total_amount >= drink_cost:
        payment_is_enough = True
        print(f"You put in {round(total_amount, decimals=2)}$. The drink costs {drink_cost}$.")
        total_change = total_amount - drink_cost
        total_change = round(total_change, decimals=2)
        print(f"Your change is {total_change}$")
    else:
        payment_is_enough = False
        print(f"You did not put enough money in: {total_amount}$. The drink costs {drink_cost}$. Returning {total_amount}$")
    return payment_is_enough, total_amount, total_change


def dispense_drink(water, milk, coffee, payment_is_enough, total_amount):
    if resources["water"] > int(water) and resources["milk"] > int(milk) and resources["coffee"] > int(coffee) and payment_is_enough == True:
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        resources_is_enough = True
        print(f"Dispensing {machine_command}. Enjoy your drink")
    elif resources["water"] < int(water) or resources["milk"] < int(milk) or resources["coffee"] < int(coffee) and payment_is_enough == True:
        print(f"Not enough resources available. Please refill. Returning {round(total_amount-total_change, decimals= 2)}$ ")
        resources_is_enough = False
        report()
    else:
        resources_is_enough = False
    return resources_is_enough


while machine_on:
    machine_command = input("What drink would you like? (espresso/latte/cappuccino) ").lower()
    if machine_command == "report":
        report()
    elif machine_command == "refill":
        refill()
    elif machine_command == "espresso" or "latte" or "cappuccino":
        payment_is_enough, total_amount, total_change = payment(MENU[machine_command]["cost"])
        dispense_drink(MENU[machine_command]["ingredients"]["water"], MENU[machine_command]["ingredients"]["milk"], MENU[machine_command]["ingredients"]["coffee"], payment_is_enough, total_amount)
    else:
        break
