from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# If length of command line argument is 1
if len(sys.argv) == 1:

    # Take user's input
    user_input = input("Input: ")

    # Choose a random font and set
    font_choice = random.choice(figlet.getFonts())
    figlet.setFont(font=font_choice)

    # Print user's input in random font
    print(figlet.renderText(user_input))


# If length of command line argument is 3 and second argument consist -f or --font
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:

    # To choose the font as user request and set
    font_choice = sys.argv[2]

    # Create a list from figlet library fonts
    list = figlet.getFonts()

    # Check if requested font not in the list 
    if font_choice not in list:

        # Print "Invalid usage" and exit the system
        sys.exit("Invalid usage")

    # Check if requested font in the list
    else:

        # Take user's input 
        user_input = input("Input: ")

        # Set the font, print and display
        figlet.setFont(font=font_choice)
        print(figlet.renderText(user_input))

# Check if command line argument is not as required exit the system and print "Invalid usage"
else:
    sys.exit("Invalid usage")
