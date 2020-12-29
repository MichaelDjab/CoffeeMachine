# Types of coffee with data needed for machine functionality
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

# Available resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def refill_collect():
    """
    Refills the machine's resources, and collects money such that initial state is reinstated
    """
    global resources
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }
    print("Machine filled up with resources, money collected.")


def resources_ok(choice):
    """
    Checks if there are enough resources, if so return True, otherwise prints the first resource that
    is missing and returns False
    :param choice:
    """
    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("\tSorry there is not enough water.")
        return False
    if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print("\tSorry there is not enough milk.")
        return False
    if resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("\tSorry there is not enough coffee")
        return False
    return True


def report():
    """
    Print report that shows the current resource values
    """
    print("\tWater: {water}ml".format(**resources))
    print("\tMilk: {milk}ml".format(**resources))
    print("\tCoffee: {coffee}g".format(**resources))
    print("\tMoney: ${money}".format(**resources))


def make_coffee(choice):
    """
    Makes coffee, by calling resources_ok() and coins_ok() and
    reducing the resources by the amount needed to make coffee
    param choice:
    """
    if resources_ok(choice) and coins_ok(choice):
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        resources["money"] += MENU[choice]["cost"]


def coins_ok(choice):
    """
    Asks user for coins and makes sure there is enough, if so prints change and returns True,
    otherwise prints that money is missing, returns False.
    :param choice:
    """
    print("Please insert coins")
    quarters = int(input("\thow many quarters?: "))
    dimes = int(input("\thow many dimes?: "))
    nickles = int(input("\thow many nickles?: "))
    pennies = int(input("\thow many pennies?: "))
    total_inserted = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    # Not enough money inserted
    if total_inserted < MENU[choice]["cost"]:
        print("\tsorry that's not enough money. Money refunded.")
        return False
    # Give back change
    else:
        change = round(100*(total_inserted - MENU[choice]["cost"]))/100.0
        print(f"\tHere is ${change} in change.")
        print(f"\tHere is your {choice} ☕️. Enjoy!")
        return True


# Program starts here
user_choice = ""
while not user_choice == "off":
    user_choice = input("What would you like? ($1.50 - espresso/$2.50 - latte/$3.00 - cappuccino):").lower()
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        break
    elif user_choice == "report":
        report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        make_coffee(user_choice)
    elif user_choice == "refill":
        refill_collect()
    else:
        print("\tInvalid choice, watch your spelling. 😉")
