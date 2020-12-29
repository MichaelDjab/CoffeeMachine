MENU = {
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# Print report that shows the current resource values
def report():
    print("Water: {water}ml".format(**resources))
    print("Milk: {milk}ml".format(**resources))
    print("Coffee: {coffee}g".format(**resources))
    print("Money: ${money}".format(**resources))


def make_coffee(choice):
    if coins_ok(choice):
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        resources["money"] += MENU[choice]["cost"]
    report()


def coins_ok(choice):
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_inserted = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

    # Not enough money inserted
    if total_inserted < MENU[choice]["cost"]:
        print("sorry that's not enough money. Money refunded.")
        return False
    # Give back change
    else:
        change = round(100*(total_inserted - MENU[choice]["cost"]))/100.0
        # TODO print 2 decimals
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice} ☕️. Enjoy!")
        return True


# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
user_choice = input("What would you like? ($1.50 - espresso/$2.50 - latte/$3.00 - cappuccino):").lower()
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
if user_choice == "off":
    exit()
# 3. Print report that shows the current resource values
elif user_choice == "report":
    report()
elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
    make_coffee(user_choice)
else:
    print("Invalid choice, watch your spelling 😉")