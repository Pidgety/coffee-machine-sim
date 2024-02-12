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
        "cost": 1.90,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.60,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 2.80,
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
    """Takes one argument - the name of a drink selected by the user
    - and returns False if any of the resources in the coffee machine
    are lower than those required to make the drink.  Returns True if
    all resources are sufficient."""
    if resources["water"] < MENU[drink]["ingredients"].get("water"):
        print("Sorry, there is not enough water.")
        return False
    if resources["milk"] < MENU[drink]["ingredients"].get("milk", 0):
        print("Sorry, there is not enough milk.")
        return False
    if resources["coffee"] < MENU[drink]["ingredients"].get("coffee"):
        print("Sorry, there is not enough coffee.")
        return False
    return True


def cash_handling(price):
    """Takes one argument - the price of the drink selected by the user.
    Informs the user of the price, and prompts user to input how many
    of each coin type they are inserting into the machine.
    Calculates total value of coins inserted and returns True
    (and the value of price) if the amount is sufficient or False 
    (and a value of 0) if insufficient."""

    print(f"Please enter £{price:.2f}")
    cash_entered = 0
    message = "\nPlease enter a number."

    pounds = input("\nNo. of one pound coins: ") #1.00
    while not pounds.isnumeric():
        print(message)
        pounds = input("\nNo. of pound coins: ")
    pounds = int(pounds)

    fifties = input("\nNo. of fifty pence coins: ") #0.50
    while not fifties.isnumeric():
        print(message)
        fifties = input("\nNo. of fifty pence coins: ")
    fifties = int(fifties)

    twenties = input("\nNo. of twenty pence coins: ") #0.20
    while not twenties.isnumeric():
        print(message)
        twenties = input("\nNo. of twenty pence coins: ")
    twenties = int(twenties)

    tens = input("\nNo. of ten pence coins: ") #0.10
    while not tens.isnumeric():
        print(message)
        tens = input("\nNo. of ten pence coins: ")
    tens = int(tens)

    cash_entered = ((pounds * 1.00) + (fifties * 0.50) +
                    (twenties * 0.20) + (tens * 0.10))

    # prompt user to enter coins - check numeric / convert to int.
    # calculate total
    if cash_entered >= price:
        change = round(cash_entered - price, 2)
        print(f"\nChange: £{change:.2f}")
        return True, price

    print(f"\nSorry, you only entered £{cash_entered:.2f} of £{price:.2f}\n"
        f"Refund: £{cash_entered:.2f}")
    return False, 0

# == MAIN ROUTINE ==
money = 0

is_on = True
while is_on:
    user_choice = input("\nWhat would you like? (espresso, latte, cappuccino): ")
    if user_choice.lower() == "off":
        print("\nCoffee machine is now off!")
        is_on = False
    elif user_choice.lower() =="report":
        print("\n\033[1mResources Report:\033[0m")
        print(f"Water:\t{resources["water"]} ml\nMilk:\t{resources["milk"]} ml")
        print(f"Coffee:\t{resources["coffee"]} g\nMoney:\t£ {money}")
    elif user_choice in MENU:
        enough_resources = check_resources(user_choice)
        if enough_resources:
            # Ask user to enter money, and handle payment
            ok_to_serve = cash_handling(MENU[user_choice]["cost"])
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
