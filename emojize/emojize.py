import emoji

# define main function ask user's input then output converted str to emoji
def main():
    str_emoji = input("Input: ")
    print(emoji.emojize(f"Python is {str_emoji}", language='alias'))

# call main function
if __name__ == "__main__":
    main()

