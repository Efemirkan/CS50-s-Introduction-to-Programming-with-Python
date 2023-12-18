def main():

    # Take user's input
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

    # If is_answer(answer) is True , print "Yes"
    if is_answer(answer):
        print("Yes")

    # If is_answer(answer) is False, print "No"
    else:
        print("No")

# Define is_answer(str) function to check conditions
def is_answer(answer):

    # Remove the whitespaces
    answer = answer.strip()

    # Check if answer = "forty-two" and return True
    if answer == "forty-two":
        return True
    
    # Check if answer = "42" or "Forty Two" after converting title form and return True
    elif answer == "42" or answer.title() == "Forty Two":
        return True
    
    # Check for all other conditions and return False
    else:
        return False

main()
