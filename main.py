"""This program simulates a coffee machine and has the following 
functionality:
    - generate a report that shows current resources
    - check available resources when user selects coffee option
            - refund if insufficent money provided
            - inform user if insufficient water, milk or sugar
    - serve coffee if resources sufficient, adjusting resources
      and providing change where applicable"""

# Day 15 project from "100 Days of Code - The Complete Python Pro
# Bootcamp" - Angela Yu, Udemy course

# ======= STARTING CODE PROVIDED ========
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
}

# ======== MY SOLUTION ========
# Please note: the code below may not be an optimal solution but reflects
# my knowledge at the time of creation (26/01/2024)

# == FUNCTIONS ==

def check_resources(drink):
    if resources["water"] < MENU[user_choice]["ingredients"].get("water"):
        print("Sorry, there is not enough water.")
        return False
    if resources["milk"] < MENU[user_choice]["ingredients"].get("milk", 0):
        print("Sorry, there is not enough milk.")
        return False
    if resources["coffee"] < MENU[user_choice]["ingredients"].get("coffee"):
        print("Sorry, there is not enough coffee.")
        return False
    return True


def cash_handling(price):
    print(f"Please enter ${price}")
    cash_entered = 0
    message = "\nPlease enter a number."

    quarters = input("\nNo. of quarters: ") #0.25
    while not quarters.isnumeric():
        print(message)
        quarters = input("\nNo. of quarters: ")
    quarters = int(quarters)

    dimes = input("\nNo. of dimes: ") #0.10
    while not dimes.isnumeric():
        print(message)
        dimes = input("\nNo. of dimes: ")
    dimes = int(dimes)

    nickels = input("\nNo. of nickels: ") #0.05
    while not nickels.isnumeric():
        print(message)
        nickels = input("\nNo. of nickels: ")
    nickels = int(nickels)

    pennies = input("\nNo. of pennies: ") #0.01
    while not pennies.isnumeric():
        print(message)
        pennies = input("\nNo. of pennies: ")
    pennies = int(pennies)

    cash_entered = ((quarters * 0.25) + (dimes * 0.10) + 
                    (nickels * 0.05) + (pennies * 0.01))

    # prompt user to enter coins - check numeric / convert to int.
    # calculate total
    if cash_entered >= price:
        change = round(cash_entered - price, 2)
        print(f"\nChange: ${change}")
        return True, price

    print(f"\nSorry, you only entered ${cash_entered} of ${price}\n"
        f"Refund: {cash_entered}")
    return False, 0

# == MAIN ROUTINE ==
money = 0

is_on = True
while is_on:
    user_choice = input("\nWhat would you like? (espresso, latte, cappucino): ")
    if user_choice.lower() == "off":
        print("\nCoffee machine is now off!")
        is_on = False
    elif user_choice.lower() =="report":
        print("\n\033[1mResources Report:\033[0m")
        print(f"Water:\t{resources["water"]} ml\nMilk:\t{resources["milk"]} ml")
        print(f"Coffee:\t{resources["coffee"]} g\nMoney:\t$ {money}")
    elif user_choice in MENU:
        enough_resources = check_resources(user_choice)
        if enough_resources:
            # Ask user to enter money, and handle payment
            ok_to_serve = cash_handling(MENU[user_choice]["cost"])
            print(ok_to_serve)
            if ok_to_serve[0]:
                money += ok_to_serve[1]
                resources["water"] -= MENU[user_choice]["ingredients"].get("water")
                resources["milk"] -= MENU[user_choice]["ingredients"].get("milk", 0)
                resources["coffee"] -= MENU[user_choice]["ingredients"].get("coffee")
                print(f"\nHere is your {user_choice}. Enjoy!")
                continue
            continue
        continue
    else:
        print("\nPlease enter a valid option.")
