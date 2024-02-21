from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_on:
    order_name = input("What would you like to drink? " + coffee_menu.get_items() + " ")
    if order_name == "off":
        machine_on = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "refill":
        coffee_maker.__init__()
    else:
        drink = coffee_menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink) == True and money_machine.make_payment(drink.cost) == True:
            coffee_maker.make_coffee(drink)
