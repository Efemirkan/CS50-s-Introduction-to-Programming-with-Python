#define main function to take user input and give expected output
def main():
    strin = input("Input: ")
    print(f"Output: {shorten(strin)}")

#remove vowels from the input create vowels as string and create an empty string to append
#letters after iterating and choosing the expected one
def shorten(str):
    new_str = ""
    remove_str = "aeiouAEIOU"
    for letter in str:
        if letter not in remove_str:
            new_str += letter
    return new_str

if __name__ == "__main__":
    main()
