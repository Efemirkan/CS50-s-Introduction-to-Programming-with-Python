def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
            if s[:2].isalpha():
                for i in range(len(s)-1):
                    if s[i].isalpha() and s[i+1] == "0":
                        return False
                    elif s[i].isdigit() and s[i+1].isalpha():
                        return False
                return True

            else:
                return False

    else:
         return False

main()
