def main():

    # Take user's input
    exp = input("Expression: ")
    x, y, z = seperate(exp)

    # Check if y = "+" sum x,z and print with 1 decimal place
    if y == "+":
        sum = x + z
        print(f"{sum:.1f}")

    # Check if y = "-" substract x,z and print with 1 decimal place
    elif y == "-":
        abs = x - z
        print(f"{abs:.1f}")

    # Check if y = "*" multiply x,z and print with 1 decimal place
    elif y == "*":
        mul = x * z
        print(f"{mul:.1f}")

    # Check if y = "/" divide x,z and print with 1 decimal place
    elif y == "/":
        
        # Check if z is not equal 0
        if z != 0:
            divide = x / z
            print(f"{divide:.1f}")
        else:
            print("Second integer can not be zero")

    # Check if input is not required format
    else:
        print("Please re-enter")

# Define seperate(exp) funtion to split expression
def seperate(exp):

    # Split exp by whitespace
    x, y, z = exp.split(" ")

    # Case x and z to integer and return all
    return int(x), y, int(z)

main()
