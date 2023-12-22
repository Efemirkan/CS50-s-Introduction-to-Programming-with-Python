# Initialized Variable
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
] #  To store months

def main():

    # While loop to ask continuously user's input
    while True:

        try:
            # Take user's input and remove whitespaces
            date = input("Date: ").strip()

            # Check if date contain "/"
            if "/" in date:
                # Call number_month(date) function and print then break the loop
                print(number_month(date))
                break

            # Check if date contain ","
            elif "," in date:
                # Call string_month(date) function and print then break the loop
                print(string_month(date))
                break

            # Check if date does not contain "," or "/" raise Value Error
            else:
                raise ValueError

        # Handle related to ValueError
        except ValueError:
            pass

# Define def number_month(date) to convert the format
def number_month(date):

    # Keep looping until a valid date is provided
    while True:
        try:
            # Split date by "/"
            list = date.split("/")
            # Check if int(list[0]) greater than 12
            if int(list[0]) > 12:
                # Raise ValueError
                raise ValueError

            # Check if int(list[1]) greater than 31
            if int(list[1]) > 31:
                # Raise ValueError
                raise ValueError

        # Handle related to ValueError
        except ValueError:
            pass

        # If no ValueError is raised, format the date and return it
        else:
            return f"{list[2]}-{int(list[0]):02}-{int(list[1]):02}"

# Define def number_month(date) to convert the format
def string_month(date):

    # Keep looping until a valid date is provided
    while True:
        try:
            # Split date by " "
            list = date.split(" ")

            # Check if list[0] formated Title not in months list
            if list[0].title() not in months:
                # Raise ValueError
                raise ValueError

            # Check if integer list[1] greater than 31
            if int(list[1].rstrip(",")) > 31:
                # Raise ValueError
                raise ValueError

            # For loop to find index of the month iterate length of the months list
            for i in range(len(months)):
                # Check if the month at the current index matches with months in user's input
                if months[i] == list[0]:
                    # Format the date and return it
                    return f"{list[2]}-{(i+1):02}-{int(list[1].rstrip(',')):02}"

        # Handle related to ValueError
        except ValueError:
            pass


main()
