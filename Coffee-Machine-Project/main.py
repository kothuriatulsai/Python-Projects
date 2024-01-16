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

machine = True
money = 0.00


def report(res):
    w = res["water"]
    m = res["milk"]
    c = res["coffee"]

    print(f"Water: {w}ml\nMilk: {m}ml\nCoffee: {c}g\nMoney: ${money}")


def espresso():
    w = resources["water"]
    m = resources["milk"]
    c = resources["coffee"]
    w -= 50
    c -= 18
    m -= 0
    resources["water"] = w
    resources["milk"] = m
    resources["coffee"] = c


def latte():
    w = resources["water"]
    m = resources["milk"]
    c = resources["coffee"]
    w -= 200
    c -= 24
    m -= 150
    resources["water"] = w
    resources["milk"] = m
    resources["coffee"] = c


def cappuccino():
    w = resources["water"]
    m = resources["milk"]
    c = resources["coffee"]
    w -= 250
    c -= 24
    m -= 100
    resources["water"] = w
    resources["milk"] = m
    resources["coffee"] = c


def calculate():
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    m = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    return m


def check_resources(res, w, m, c):
    water_left = res["water"] - w
    milk_left = res["milk"] - m
    coffee_left = res["coffee"] - c
    if water_left >= 0 and milk_left >= 0 and coffee_left >= 0:
        return True
    else:
        return False


def no_resources(res, w, m, c, coffee):
    water_left = res["water"] - w
    milk_left = res["milk"] - m
    coffee_left = res["coffee"] - c
    if water_left < 0 and milk_left < 0 and coffee_left < 0:
        print(f"Sorry, There is no water, milk and coffee required for the {coffee}")
    elif water_left < 0 and milk_left < 0:
        print(f"Sorry, There is no water and milk required for the {coffee}.")
    elif water_left < 0 and coffee_left < 0:
        print(f"Sorry, There is no water and coffee required for the {coffee}.")
    elif coffee_left and milk_left < 0:
        print(f"Sorry, There is no coffe and milk required for the {coffee}.")
    elif water_left < 0:
        print(f"Sorry, There is no water required for the {coffee}.")
    elif milk_left < 0:
        print(f"Sorry, There is no milk required for the {coffee}.")
    elif coffee_left < 0:
        print(f"Sorry, There is no water required for the {coffee}.")


while machine:
    user = input("What would you like? (espresso/latte/cappuccino): ")
    if user == "off":
        machine = False
    elif user == "espresso":
        if check_resources(resources, 50, 0, 18):
            me = calculate()
            if me >= 1.50:
                ch = round(me - 1.50, 2)
                print(f"Here is ${ch} in change.")
                money += 1.50
                espresso()
                print("Here is your espresso ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            no_resources(resources, 50, 0, 18, "espresso")
    elif user == "cappuccino":
        if check_resources(resources, 250, 100, 24):
            mc = calculate()
            if mc >= 3.00:
                ch = round(mc - 3.00, 2)
                print(f"Here is ${ch} in change.")
                money += 3.00
                cappuccino()
                print("Here is your cappuccino ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            no_resources(resources, 250, 100, 24, "cappuccino")
    elif user == "latte":
        if check_resources(resources, 200, 150, 24):
            ml = calculate()
            if ml >= 2.50:
                ch = round(ml - 2.50, 2)
                print(f"Here is ${ch} in change.")
                money += 2.50
                latte()
                print("Here is your latte ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            no_resources(resources, 200, 150, 24, "latte")
    elif user == "report":
        report(resources)
