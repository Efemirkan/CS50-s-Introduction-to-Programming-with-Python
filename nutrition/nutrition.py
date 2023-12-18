fruits = {
    "Apple" : 130,
    "Avocado" : 50,
    "Banana" : 110,
    "Cantaloupe" : 50,
    "Grapefruit" : 60,
    "Grapes" : 90,
    "Honeydew Melon" : 50,
    "Kiwifruit" : 90,
    "Lemon" : 15,
    "Lime" : 20,
    "Nectarine" : 60,
    "Orange" : 80,
    "Peach" : 60,
    "Pear" : 100,
    "Pineapple" : 50,
    "Plums" : 70,
    "Strawberries" : 50,
    "Sweet Cherries" : 100,
    "Tangerine" : 50,
    "Watermelon" : 80
}

# Define main() function to take user's input, and print and display calories
def main():
    # Take user's input
    item = input("Item: ")
    # Check if user's input from data
    if calculate(item):
        print(f"Calories: {calculate(item)}")
    # If user's input out of data
    else:
        print(f"")

# Define calculate() funtion to return item's value
def calculate(fruit):
    # Formating variable
    fruit = fruit.strip().title()
    # For loop that iterates over fruits dictionary and return each fruit's calories
    for item in fruits:
        if item == fruit:
            return fruits[fruit]
    # If out of data
    return False

main()

