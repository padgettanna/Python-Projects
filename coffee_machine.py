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
money = 0
water_available = resources["water"]
milk_available = resources["milk"]
coffee_available = resources["coffee"]
turn_off = False


def report():
    return f"Water: {water_available}ml\nMilk: {milk_available}ml\nCoffee: {coffee_available}g\nMoney: ${money}"


while not turn_off:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "off":
        turn_off = True
    elif answer == "report":
        print(report())
    elif answer == "espresso" or "latte" or "cappuccino":
        water_for_drink = MENU[answer]["ingredients"]["water"]
        coffee_for_drink = MENU[answer]["ingredients"]["coffee"]
        cost_of_drink = MENU[answer]["cost"]
        if answer == "espresso":
            milk_for_drink = 0
        else:
            milk_for_drink = MENU[answer]["ingredients"]["milk"]

        if water_available >= water_for_drink and coffee_available >= coffee_for_drink and milk_available >= milk_for_drink:
            print("Please insert coins")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            money_inserted = round((quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01), 2)

            if money_inserted < cost_of_drink:
                print("Sorry, not enough money. Money refunded.")
            else:
                water_available = water_available - water_for_drink
                milk_available = milk_available - milk_for_drink
                coffee_available = coffee_available - coffee_for_drink
                change = round((money_inserted - cost_of_drink), 2)
                money += money_inserted - change

                print(f"Here is ${change} in change.")
                print(f"Here is your {answer} ☕️. Enjoy!")
        elif water_available < water_for_drink:
            print(f"Sorry, not enough water.")
        elif coffee_available < coffee_for_drink:
            print(f"Sorry, not enough coffee.")
        elif milk_available < milk_for_drink:
            print(f"Sorry, not enough milk.")
