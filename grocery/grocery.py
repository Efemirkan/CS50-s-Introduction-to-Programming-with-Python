# Define main() funtion to display user's input as required
def main():

    # Initialize variable
    counted =[]  # to store amount of items

    # Take user's input
    items = ask_user("")

    # For loop to iterate through the items and count each item then append to counted list
    for item in items:
        # Call count() method to count items
        m = items.count(item)
        counted.append(m)

    # Create a dict from item and counted list
    grocery_list = dict(zip(items, counted))

    #For loop to iterate and sort alphabetically  grocery_list dict
    for key in sorted(grocery_list):
        # Print and display format "1 Apple"
        print(f"{grocery_list[key]} {key.upper()}")

# Define ask_user(prompt) function with prompt argument
def ask_user(prompt):

    # Initialize variable
    items = []  # to store user input

    # While loop to ask continuously
    while True:

        # Except EOFError take user's input and append to items list
        try:
            item = input(prompt)
            items.append(item)

        # EOFError return items
        except EOFError:
            return items

if __name__ == "__main__":
    main()



