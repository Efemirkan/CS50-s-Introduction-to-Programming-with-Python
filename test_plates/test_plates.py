from plates import is_valid

def test_isvalid():

    # Test: Valid plate with alphabetical characters followed by numeric character not "0"
    assert is_valid("CS50") == True

    # Test: Invalid plate with alphabetical characters followed by "0"
    assert is_valid("CS05") == False

    # Test: Invalid plate with alphabetical characters followed by numeric characters then again alphabetical character
    assert is_valid("CS50P") == False

    # Test: Invalid plate with non-alphanumeric character "."
    assert is_valid("PI3.14") == False

    # Test: Invalid plate with less than character
    assert is_valid("H") == False

    # Test: Invalid plate with more than 6 characters
    assert is_valid("HARVARDCS50") == False

    # Test: Valid plate with only two alphabetical characters
    assert is_valid("CS") == True

    # Test: Invalid plate with more than 6 only alphabetical acharacters
    assert is_valid("OUTATIME") == False

    # Test: Invalid plate with beginning with numerical character
    assert is_valid("50") == False

