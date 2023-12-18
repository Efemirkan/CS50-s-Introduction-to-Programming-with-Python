import sys

# If does not have command line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# If more than 1 command line argument
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# For loop to access command line argument
for arg in sys.argv[1:]:
    #If file extension is not .py
    if arg[-3:] != ".py":
        sys.exit("Not a Python file")

    try:
        # To open file
        with open(arg) as file:
            count = 0  # Initilize variable to store count for loop
            for line in file:
                #If not line white blank and if not has comment
                if line.lstrip()[:1] != "#" and len(line.strip()) != 0:
                    count += 1  # Update count
        # Print and display count
        print(count)
        
    # Raise FileNotFoundError
    except FileNotFoundError:
        print("File does not exist")




