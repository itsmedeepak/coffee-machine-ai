from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    option = Menu().get_items()
    get_cmd = input(f"What would you like? ({option}):")
    if get_cmd == "off":
        is_on = False
    elif get_cmd == "report":
        CoffeeMaker().report()
    else:
        drink = Menu().find_drink(get_cmd)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)