def is_valid(plate):
    # Check length
    if not (2 <= len(plate) <= 6):
        return False

    # Check if it starts with at least two letters
    if not plate[:2].isalpha():
        return False

    # Check for valid characters and numbers rule
    if not valid_characters_and_numbers(plate):
        return False

    return True


def valid_characters_and_numbers(plate):
    found_number = False

    for i, char in enumerate(plate):
        # No punctuation, spaces, or periods allowed
        if not char.isalnum():
            return False

        # If we find a digit
        if char.isdigit():
            if found_number == False:  # This is the first digit encountered
                if char == '0':  # First number can't be '0'
                    return False
                found_number = True
        else:
            if found_number:  # If a letter is found after a number, it's invalid
                return False

    return True


# Main logic
plate = input('Plate: ').upper().strip()

if is_valid(plate):
    print('Valid')
else:
    print('Invalid')