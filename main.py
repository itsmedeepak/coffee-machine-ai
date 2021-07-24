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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(coffee_name):
    for items in resources:
        drink = MENU[coffee_name]['ingredients']
        if resources[items] < drink[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def make_coffee(coffee_name):
    drink = MENU[coffee_name]['ingredients']
    for item in resources:
        resources[item] -= drink[item]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")


def transaction(coffee_name):
    print("Please insert coins.")
    quarter = int(input("how many quarters?:"))
    dim = int(input("how many dimes?:"))
    nick = int(input("how many nickles?:"))
    penni = int(input("how many pennies?:"))
    cal = quarter * 0.25 + dim * 0.1 + nick * 0.05 + penni * 0.01
    actual = MENU[coffee_name]["cost"]
    if actual == cal:
        print("Transaction is successful")
        if is_sufficient(coffee_name):
            make_coffee(coffee_name)
    elif actual < cal:
        keep_change = round(cal - actual)
        print(f"Here is ${keep_change} in change.")
        print("Transaction is successful\n")
        if is_sufficient(coffee_name):
            make_coffee(coffee_name)
        else:
            print(f" $ {cal} Money refunded.")
    else:
        print(f"Sorry that's not enough money. $ {cal} Money refunded.")


exit_ = False
while not exit_:
    get_cmd = input("What would you like? (espresso/latte/cappuccino):")
    if get_cmd == 'report':
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
    elif get_cmd == 'off':
        print("session is terminated")
        exit_ = True
    elif get_cmd == 'espresso':
        transaction('espresso')
    elif get_cmd == 'latte':
        transaction('latte')
    elif get_cmd == 'cappuccino':
        transaction('cappuccino')
    else:
        print("you enter a invalid key")
