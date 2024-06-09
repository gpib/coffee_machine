import boundaries

def check_resources(order_ingredients):
    for item in order_ingredients:
        print(item)
    if (order_ingredients['ingredients']['water']) <= boundaries.resources['water'] and \
        (order_ingredients['ingredients']['milk']) <= boundaries.resources['milk'] and \
        (order_ingredients['ingredients']['coffee']) <= boundaries.resources['coffee']:
        print("OK")
        print(f"Was water {boundaries.resources['water']}")
        boundaries.resources['water'] = boundaries.resources['water'] - (order_ingredients['ingredients']['water'])
        print(f"Is water {boundaries.resources['water']}")
    else:
        print("NOK")
    return 0

# TODO 1. Print report

machine_on = True

while machine_on:
    user_choice = input("What would you like to drink?").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {boundaries.resources['water']}")
        print(f"Milk: {boundaries.resources['water']}")
        print(f"Coffee: {boundaries.resources['water']}")
    else:
        drink = boundaries.MENU[user_choice]
        check_resources(drink['ingredients'])







