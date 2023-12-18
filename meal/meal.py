def main():

    # Take user's input
    time_input = input("what time is it? ")

    # Call convert(time) funtion and Case return value to float
    num_convert = float(convert(time_input))

    # Check if num_convert >= 7 and num_convert <= 8 print "breakfast time"
    if num_convert >= 7 and num_convert <= 8:
        print("breakfast time")

    # Check if num_convert >= 12 and num_convert <= 13 print "lunch time"
    elif num_convert >= 12 and num_convert <= 13:
        print("lunch time")

    # Check if num_convert >= 18 and num_convert <= 19 print "dinner time"
    elif num_convert >= 18 and num_convert <= 19:
        print("dinner time")
 
    
# Define convert(time) function to split time string to hours, minute and return as format required
def convert(time):

    # Split time argument by ":"
    hours, minutes = time.split(":")

    # Case minutes to integer and adjust based on a :60 ratio
    minutes = int(int(minutes) * (5 / 3))

    # Check if minutes % 10 = 0 and minutes != 00 delete zeros from right else return as it is
    return f"{hours}.{str(minutes).rstrip('0') if minutes % 10 == 0 and minutes != 00 else minutes}"

if __name__ == "__main__":
    main()
