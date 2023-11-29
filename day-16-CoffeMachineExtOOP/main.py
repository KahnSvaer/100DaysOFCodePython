from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"\nWhat would you like? {menu.get_items()}\b: ").strip().lower()
    item = None
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print("Turning OFF")
        is_on = False
    else:
        item = menu.find_drink(choice)

    if item is not None:
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)


