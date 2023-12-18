#define main function to take name of variable and outputs the corresponding name in snake case.
def main():
    case = input("camelCase: ")
    print(f"snake_case: {convert(case)}")

#define convert function to convert name of variable camelCase to snake_case
def convert(str):
    #create empty string to append to new case
    new_str = ""
    #iterate over the string to access value required
    for letter in str:
        #find uppercase letter then convert it lowercase and add _ into left
        if letter.isupper() :
            new_str += f"_{letter.lower()}"
        #other letter return as it is and append new_str
        else:
            new_str += letter
    return new_str

main()
