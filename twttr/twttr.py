def main():

    # Take user's input and print to display
    str = input("Input: ")
    print(f"Output: {remove(str)}")

# Define remove(str) to remove vowels from string
def remove(str):

    # Initialize Variale
    new_str = ""  # To store new string object
    vowels = "aAeEiIoOuU"  # Storing vowels

    # For loop to iterate each letter in string
    for letter in str:
        # If letter not in vowels string
        if letter not in vowels:
            # Concatenate to new_str
            new_str += letter
    return new_str

main()
