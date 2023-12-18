def main():

    # Take user's input
    x, y = get_input("Fraction: ")

    # Call fuel() funtion to print and display
    fuel(x, y)

# Define get_input(prompt) function to Handle with Errors and check situation fuel filled more than %100
def get_input(prompt):

    # While loop to ask continiously for prompt
    while True:

        # Take user's input and split by "/"
        try:
            x, y = input(prompt).split("/")

            # Case to integer
            x = int(x)
            y = int(y)

        # Handle releated to ValueError and ZeroDivisionError
        except (ValueError, ZeroDivisionError):
            pass

        # Without error continue
        else:
            # Check if first integer equal or less than second integer
            if x <= y:
                return x, y
            else:
                pass

# Define fuel(x, y) funtion to print fraction
def fuel(x, y):

    # Calculate fraction and round nearest integer
    fraction = round((x / y) *100)

    # Check if fraction = 0 or 1 print "E"
    if fraction == 0 or fraction == 1:
        print("E")

    # Check if fraction = 99 or 100 print "F"
    elif fraction == 99 or fraction == 100:
        print("F")

    # In other conditions print fraction%
    else:
        print(f"{fraction}%")


main()
