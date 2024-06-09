import boundaries

def check_resources(order_ingredients):
    for item in order_ingredients:
        print(item)
        print(order_ingredients[item])
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


def process_coins():
    print("inser coins")
    total = int(input("How many quarter:")) * 0.25
    total += int(input("How many dimes:")) * 0.10
    total += int(input("How many nickels:")) * 0.05
    total += int(input("How many pennies:")) * 0.01
    return total

def is_payment_successful(money_received, drink_cost):
    """Retrurn True when the payment accpted or False when insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        boundaries.balance = boundaries.balance + drink_cost
        print(f"here is your change {change}")
        return True
    else:
        print(f"not enough money, take your {money_received}")
        return False

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
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
                update_resources(drink)
            else:
                print(f"Money refunded")
        else:
            print(f"Sorry, we can't serve your {choice}")










