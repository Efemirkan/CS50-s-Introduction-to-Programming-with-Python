# Take user's input, convert lower case, and remove whitespaces
greeting = input("Greeting: ").lower().strip()

# Check If first 5 letter = "hello" and print $0
if greeting[0:5] == "hello":
    print("$0")

# Check If first letter = "h" and print $0
elif greeting[0] == "h" and greeting[0:5] != "hello":
    print("$20")

# Check if ither conditions print $100
else:
    print("$100")
