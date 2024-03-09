import os

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def operate_machine():
    os.system("cls")
    order = input(f"What would you like? ({menu.get_items()}): ").strip().lower()

    if order == "report":
        coffee_maker.report()
        money_machine.report()

    elif order == "off":
        pass

    else:
        item = menu.find_drink(order)
        if item is not None and coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)

    if order != "off":
        input()
        operate_machine()


operate_machine()
