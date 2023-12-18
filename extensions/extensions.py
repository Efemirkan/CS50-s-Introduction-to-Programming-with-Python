#user input file name case-insensitively and without whiteblank
def main():

    # Take user's input
    file_name = input("Please enter the file name: ").lower().strip()

    # Call extension(file_name) to get the extension
    ext = extension(file_name)

    # Check if ext == "png" or "gif" and print image/ext
    if ext == "png" or ext == "gif":
        print(f'image/{ext}')

    # Check if ext == "jpg" or "jpeg" and print image/jpeg
    elif ext == "jpg" or ext == "jpeg":
        print("image/jpeg")

    # Check if ext == "pdf" or "zip" and print application/ext
    elif ext == "pdf" or ext == "zip":
        print(f'application/{ext}')

    # Check if ext == "txt" and print text/plain
    elif ext == "txt":
        print(f'text/plain')

    # In all other conditions print application/octet-stream
    else:
        print("application/octet-stream")

# Define extension(file) to find the extension
def extension(file):
    
    # Check if "." in file's name
    if "." in file:

        # Split only one time file's name from right by "."
        ext = file.rsplit(".", maxsplit= 1)

        # Return second element 
        return ext[1]
    
    # if file's name has no extension return ""
    else:
        return ""

main()
