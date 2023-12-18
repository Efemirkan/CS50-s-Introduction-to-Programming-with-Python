import inflect

p = inflect.engine()

def main():
    # Initilize Variable
    list = []  # to store names
    # Handle with EOFError
    try:
        # Loop through until EOFError
        while True:
            # Take user's input and append to the list
            name = input("Name: ")
            list.append(name)
    # If EOFError occurs, call adieu(list) to print the return string
    except EOFError:
        print(f"\n {adieu(list)}")

# Define adieu(list) function to check length of list
def adieu(list):
    # If length of list == 1, return f"Adieu, adieu, to name"
    if len(list) == 1:
        return f"Adieu, adieu, to {list[0]}"
    # If length of list == 2, return f"Adieu, adieu, to name1 and name2"
    elif len(list) == 2:
        mylist = p.join(list)
        return f"Adieu, adieu, to {mylist}"
    # If length of list == 2, return f"Adieu, adieu, to name1, name2, and name3"
    elif len(list) > 2:
        mylist = p.join(list)
        return f"Adieu, adieu, to {mylist}"

if __name__ == "__main__":
    main()
