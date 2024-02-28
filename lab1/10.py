def check_character_type(char):
    if len(char) != 1:
        print("Error: Input should contain only one character.")
        return -1
    elif char.isalpha():
        return 0  # Alphabetic
    elif char.isnumeric():
        return 1  # Numeric
    else:
        return -1  # Neither alphabetic nor numeric

