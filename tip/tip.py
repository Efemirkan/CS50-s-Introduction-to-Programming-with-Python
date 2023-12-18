def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    str1 = d.strip("$")
    return float(str1)


def percent_to_float(p):
    str2 = float(p.strip("%")) / 100
    return (str2)


main()
