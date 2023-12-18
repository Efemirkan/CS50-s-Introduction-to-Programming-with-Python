def main():

    # Initialize variable
    i = 50  # to store budget

    # While loop to ask users continiously insert money until they do not have
    while True:

        coin = get_input(i)
        i -= coin  # in every loop substract the coin from the budget

        # Check if how much change owed after users spend whole budget
        if i <= 0:
            print(f"Change Owed: {-i}")
            break

# Define get_input function to take user's input and and check conditions
def get_input(amountdue):

    # Whlie loop to ask continiously 
    while True:
        coin = int(input(f"Amount Due: {amountdue}\nInsert Coin: "))

        # Check if coin = 5, 10 or 25 return coin
        if coin == 5 or coin == 10 or coin == 25:
            return coin
        
        # In other conditions return 0
        else:
            return 0

main()
