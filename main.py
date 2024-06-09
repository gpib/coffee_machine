import boundaries

def check_resources(order_ingredients):
    for item in order_ingredients:
        print(item)
    if (order_ingredients['ingredients']['water']) <= boundaries.resources['water'] and \
        (order_ingredients['ingredients']['milk']) <= boundaries.resources['milk'] and \
        (order_ingredients['ingredients']['coffee']) <= boundaries.resources['coffee']:
        print("OK, enough supplies")
        return True
    else:
        print("NOK, not enough supplies")
        return False
def update_resources(order_ingredients):
    for item in order_ingredients:
        boundaries.resources['water'] = boundaries.resources['water'] - (order_ingredients['ingredients']['water'])
        boundaries.resources['milk'] = boundaries.resources['milk'] - (order_ingredients['ingredients']['milk'])
        boundaries.resources['coffee'] = boundaries.resources['coffee'] - (order_ingredients['ingredients']['coffee'])
        boundaries.balance = boundaries.balance + (order_ingredients['cost'])

is_on = True
while is_on:
    choice = input("What would youe like? (espresso, latte, cappuccino)")
    if choice.lower() == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {boundaries.resources['water']}ml")
        print(f"Milk: {boundaries.resources['milk']}ml")
        print(f"Coffee: {boundaries.resources['coffee']}g")
        print(f"Money: ${boundaries.balance}")
    else:
        drink = boundaries.MENU[choice]
        print(drink)
        if check_resources(drink) == True:
            print(f"Here is your {choice}")
            update_resources(drink)
        else:
            print(f"Sorry, we can't serve your {choice}")










