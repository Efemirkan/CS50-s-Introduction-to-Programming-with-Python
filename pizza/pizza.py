import sys
from tabulate import tabulate
import csv

def main():
    # If does not have command line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    # # If have more than 1 command line argument
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # If file extension is not .csv
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # If file does not exist
    if sys.argv[1] not in ["sicilian.csv","regular.csv"]:
        sys.exit("File does not exist")

    # If command line argument is "sicilian.csv"
    if sys.argv[1] == "sicilian.csv":
        table_tabulate("sicilian.csv", "Sicilian Pizza")

    # If command line argument is "regular.csv"
    elif sys.argv[1] == "regular.csv":
        table_tabulate("regular.csv", "Regular Pizza")

# Defina table_tabulate function to format and display as tabulate grid table
def table_tabulate(filename, firstrow):
    # Initialize variable
    pizzas = []  # to store menu

    # Open the file specified in first command line argument
    with open(filename) as file:
        # Read CSV file as dictionary
        reader = csv.DictReader(file)

        # For loop to iterate reader dictionary and apppend to pizzas list
        for row in reader:
            pizzas.append({firstrow : row[firstrow], "Small": row["Small"], "Large": row["Large"]})

    table = []  # to store table
    headers = [firstrow, "Small", "Large" ]  # to store headers

    # For loop to iterate pizzas list access each element and append to table list
    for pizza in pizzas:
        table.append([pizza[firstrow], pizza["Small"], pizza["Large"]])

    # Print and display as tabulate grid table
    print(tabulate(table, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
