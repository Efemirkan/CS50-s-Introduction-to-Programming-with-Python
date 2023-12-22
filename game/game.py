import random


def main():

    # Take user's input and print to display
    level = expection(input("Level: "))
    print(guess(level))

# Define expection(prompt) to handle with unexpected user's input
def expection(prompt):

    # Keep looping until a valid date is provided
    while True:
        try:

            # Case prompt parameter to integer
            level = int(prompt)

            # Check if level less than or equal to 0 , raise ValueError
            if level <= 0 :
                raise ValueError

            # Else return level
            return level

        # Handle related to ValueError
        except ValueError:
            pass

# Define guess(n) funtion to pick a number and ask to user to guess it
def guess(n):

    # Pick a number between 1 to n
    number = random.randint(1, n)

    # Keep looping until a valid date is provided
    while True:
        try:
            # Take user's input
            guess = int(input("Guess: "))
            # Check if guess less than or equal 0 raise ValueError
            if guess <= 0:
                raise ValueError

            # Check if user's unput greater than n attribute , raise ValueError
            elif guess > n :
                raise ValueError

        # Handle related to ValueError
        except ValueError:
            pass

        # If no ValueError is emerged
        else:

            # Check if user's input equal the number picked randomly
            if guess == number:
                # Return "Just right!"
                return "Just right!"

            # Check if user's input greater than the number picked randomly
            elif guess > number:
                # Return "Too large!"
                return "Too large!"

            else:
                # Else return "Too small!"
                return "Too small!"


main()
