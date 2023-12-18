import sys
import csv

# If does not have or have 1 command line argument
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

# If have more than 2 command line argument
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Attempt to open the file in 'r' (read) mode
try:
    with open(sys.argv[1]):
        pass

# Handle with the FileNotFoundError exception
except FileNotFoundError:

    # If the file is not found, exit the program with an error message
    sys.exit(f"Could not read {sys.argv[1]}")

# If no exception occurred, execute the following block
else:

    # Initialize variable
    students =[] # to store

    # Open the file specified in first command line argument
    with open(sys.argv[1]) as file:
        # Read file as dictionary
        reader = csv.DictReader(file)

        # For loop to iterate through rows
        for row in reader:
            # Assign house coloum to house variable
            house = row["house"]

            # Split name coloum by , and assign last and first variables
            last, first = row["name"].strip().split(",")

            # Append to student list formatted dictionary
            students.append({"first" : first.strip(), "last" : last.strip(), "house" : house})

    # Open the file specified in second command line argument to write
    with open(sys.argv[2], "w") as file:

        # Define the header for the CSV file
        writeheader = ["first", "last", "house"]

        # Create a CSV DictWriter object to write to the file using the specified header
        writer = csv.DictWriter(file, fieldnames=writeheader)

        # Write the header to the CSV file
        writer.writeheader()

        # For loop to iterate through the list of students and write each student's information to the CSV file
        for student in students:
            writer.writerow({"first" : student["first"], "last" : student["last"], "house" : student["house"]})
