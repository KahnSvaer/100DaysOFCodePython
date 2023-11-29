from Resources import MENU, resources


def report():
    for i in resources:
        print(f"{i}: {resources[i]}")


def subtract_value(resources_left, item, direction=1):
    insufficient_resource = []
    for i in resources_left:
        if i in item["ingredients"]:
            resources_left[i] -= direction * item["ingredients"][i]
            if resources_left[i] < 0:
                insufficient_resource.append(i)
    resources_left["money"] += direction * item["cost"]
    if len(insufficient_resource):  # 0 meaning false, else True
        for i in resources_left:
            resources_left[i] += item["ingredients"][i]
    return insufficient_resource


def coins_collected(item):
    print("Please enter the coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    money_received = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    money_to_return = money_received - item["cost"]
    if money_to_return >= 0:
        print(f"Here's your change: ${round(money_to_return, 2)}")
        return True
    else:
        return False


def coffee_machine():
    requested_item = input("\nWhat would you like to order? (espresso/latte/cappuccino) ").lower().strip()
    if requested_item == 'report':
        report()
    elif requested_item in MENU:
        insufficient_resources_left = subtract_value(resources, MENU[requested_item])
        if not len(insufficient_resources_left):
            collection = coins_collected(MENU[requested_item])
            if collection:
                print(f"Here's your {requested_item}. Enjoy!")
            else:
                print(f"Money not sufficient. Money Refunded")
                subtract_value(resources, MENU[requested_item], direction=-1)
        else:
            print(f"Not enough {insufficient_resources_left[0]}")
    elif requested_item == "off":  # Will later turn off the machine
        pass
    else:
        print("Sorry we don't have that\n")

    if requested_item != 'off':  # Turns off the machine
        coffee_machine()


coffee_machine()
