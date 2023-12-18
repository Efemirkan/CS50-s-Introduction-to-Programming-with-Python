def main():

    # Take user's inputs
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculate the tip and print with 2 decimal place
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Define dollars_to_float(d) function to return float value
def dollars_to_float(d):

    # Remove "$" from the right
    str1 = d.strip("$")
    return float(str1)

# Define percent_to_float(p) funtion to return float value
def percent_to_float(p):

    # Remove "%" from the right and adjust to float
    str2 = float(p.strip("%")) / 100
    return (str2)


main()
