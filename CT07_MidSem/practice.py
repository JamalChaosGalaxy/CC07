def is_valid_car_id(car_id):
    car_id = car_id.upper()  # Make sure it's all uppercase

    if not car_id[-1].isalpha():
        return False  # Must end with a letter

    checksum_letter = car_id[-1]
    body = car_id[:-1]

    # Extract prefix letters and numbers
    letters = ""
    numbers = ""
    for char in body:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
        else:
            return False  # Invalid character

    if len(letters) < 2:
        return False  # At least 2 letters are needed before the numbers

    # Get the last 2 letters before the number
    letter1 = letters[-2]
    letter2 = letters[-1]

    # Convert to numbers (A=1, ..., Z=26)
    l1 = ord(letter1) - ord('A') + 1
    l2 = ord(letter2) - ord('A') + 1

    # Pad number with leading zeros to ensure 4 digits
    numbers = numbers.zfill(4)

    if len(numbers) != 4 or not numbers.isdigit():
        return False

    n1 = int(numbers[0])
    n2 = int(numbers[1])
    n3 = int(numbers[2])
    n4 = int(numbers[3])

    # Apply the weighting
    total = l1 * 9 + l2 * 4 + n1 * 5 + n2 * 4 + n3 * 3 + n4 * 2

    remainder = total % 19

    # Checksum lookup
    checksum_table = [
        'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M',
        'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B'
    ]

    return checksum_letter == checksum_table[remainder]




