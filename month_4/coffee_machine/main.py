from random import choice

print("Hello World!")

# ------Program Requirements-----
#1.  Print report
#2.  Check resources sufficient?
#3.  Process coins
#4.  Check transaction successful?
#5.  Make Coffee

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
    "coffee": 100
}

# TO_DO Tracking is a very handy feature of Python

# Let the user be able to make their choice and the machine be turned off if need be.
is_on = True
while is_on:
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
