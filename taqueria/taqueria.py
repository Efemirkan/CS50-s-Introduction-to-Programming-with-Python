menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    try:
        # Initialize Variable
        total = 0  # To store total value of items

        # While loop to ask users and print continuously until EOFError
        while True:

            # Take user's input
            price = get_input("Item: ")            
            total += float(price)  # increase to total by mew item price

            # Print and display total with 2 decimal place
            print(f"Total: ${total:.2f}")

    # Handle releated to EOFError
    except EOFError:
        # If EOFError return new empty line
        return "\n"

# Define get_input(prompt) funtion to handle with errors
def get_input(prompt):

    # While loop to ask user continuously ask user for valid input
    while True:
        try:
            # Take user's input and format it Title
            item = input(prompt).title()
            price = menu[item]

        # Handle with KeyError.
        except KeyError:
            pass

        else:
            # For loop to iterate menu dictionary keys
            for k in menu:
                # Check if user's input is in dictionary
                if k != item:
                    pass
                else:
                    # If from dictionary return price
                    return price

if __name__ == "__main__":
    main()
