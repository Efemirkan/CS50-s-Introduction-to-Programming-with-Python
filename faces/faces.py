def main():

    #Take user's input
    string = input("Please enter your text: ")

    # Call convert() funtion and print 
    print(convert(string))

# Define convert(text) funtion to replace faces
def convert(text):

    # Find :( or :) in text and replace with faces
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()
