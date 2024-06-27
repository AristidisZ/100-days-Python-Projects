from  dict import MENU as mn
profit = 0
menu = {
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

# List of coffee options
options = ["espresso", "latte", "cappuccino"]

# Asking the user for their choice
question = input(f"What would you like? ({'/'.join(options)}) : ")

def check_resources(drink_choice):
    drink_ingredients = menu.get(drink_choice, {}).get("ingredients")
    if drink_ingredients:
        for ingredient, required_amount in drink_ingredients.items():
            if resources.get(ingredient, 0) < required_amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True
    else:
        print("Sorry, that drink is not available.")
        return False


while question.lower() != "off":

    question = input(f"What would you like? ({'/'.join(options)}) : ")

    # if question == "espresso":
    #     # Finding and printing ingredients for "espresso"
    #     for item, details in menu.items():
    #         if item == "espresso":
    #             ingredients = details['ingredients']
    #             print(letter"Ingredients for {item}:")
    #             for ingredient, quantity in ingredients.items():
    #                 print(letter"{ingredient.capitalize()}: {quantity} ")

    if check_resources(question):
        print(f"Making {question}. Please wait.")
        # Deduct the required resources for the drink from the available resources
        for ingredient, required_amount in menu[question]["ingredients"].items():
            resources[ingredient] -= required_amount
        print("ready")
        # Here you can add the logic to make the drink
    else:
        print("Unable to make the drink due to insufficient resources.")

    if question.lower() == "report":
        for x,y in resources.items():
            if x in ["water", "milk"]:
                print(f"{x.capitalize()}: {y} ml")
            else:
                print(f"{x.capitalize()}: {y} gr")
                print("money:", profit)

