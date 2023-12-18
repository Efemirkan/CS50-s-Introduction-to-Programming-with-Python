
def main():

    # Take user's input
    mass = int(input("Please enter mass in kilogram: "))

    # Call energy function and print the return value
    print(energy(mass))

# Define energy(m) to calculate and return e, Energy
def energy(m):

    c = 300000000  # to store speed of light
    e = m * (c**2)  # formula e = m(c**2)
    return e
main()
