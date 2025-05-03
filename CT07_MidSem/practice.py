# def is_valid_car_id(car_id):
#     # Convert input to uppercase to handle lowercase inputs
#     car_id = car_id.upper()

#     # Check if the last character is an alphabet (checksum letter)
#     if not car_id[-1].isalpha():
#         return False

#     # Extract the last letter (checksum letter)
#     checksum_letter = car_id[-1]

#     # Extract the body part (everything except the last letter)
#     body = car_id[:-1]

#     # Separate letters and digits from the body
#     letters = ""
#     numbers = ""
#     for char in body:
#         if char.isalpha():
#             letters += char  # Collect all letters
#         elif char.isdigit():
#             numbers += char  # Collect all digits
#         else:
#             return False  # Invalid character found

#     # There must be at least 2 letters before the numbers
#     if len(letters) < 2:
#         return False

#     # Get the last 2 letters before the numbers
#     letter1 = letters[-2]
#     letter2 = letters[-1]

#     # Convert the 2 letters to their position in the alphabet (A=1, ..., Z=26)
#     l1 = ord(letter1) - ord('A') + 1
#     l2 = ord(letter2) - ord('A') + 1

#     # Pad the number with zeros to make sure it has 4 digits
#     numbers = numbers.zfill(4)

#     # Extract each digit separately
#     n1 = int(numbers[0])
#     n2 = int(numbers[1])
#     n3 = int(numbers[2])
#     n4 = int(numbers[3])

#     # Multiply according to the fixed weights: 9, 4, 5, 4, 3, 2
#     total = l1 * 9 + l2 * 4 + n1 * 5 + n2 * 4 + n3 * 3 + n4 * 2

#     # Calculate the remainder when divided by 19
#     remainder = total % 19

#     # Checksum lookup table based on remainder
#     checksum_table = [
#         'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M',
#         'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B'
#     ]

#     # Compare the expected checksum letter with the one in the ID
#     if checksum_letter == checksum_table[remainder]:
#         return True

# # === Main Program ===

# # Ask the user for the car registration plate
# car_plate = input("Registration Plate: ")

# # Call the validation function and print the result
# if is_valid_car_id(car_plate):
#     print("Valid")
# else:
#     print("Invalid")


def check_registration_plate(board):
    board = board.upper()

    if not board[-1].isalpha:
        return False

    check_sum_letter = board[-1]

    Body = board[:-1]

    letters = ""
    numbers = ""
    for char in Body:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
        else:
            return False
        
    if len(letters) < 2:
        return False
    
    letter1 = letters[-2]
    letter2 = letters[-1]
    
    l1 = ord(letter1) - ord('A') + 1
    l2 = ord(letter2) - ord('A') + 1

    numbers = numbers.zfill(4)

    Number1 = int(numbers[0])
    Number2 = int(numbers[1])
    Number3 = int(numbers[2])
    Number4 = int(numbers[3])

    total = l1 * 9 + l2 * 4 + Number1 * 5 + Number2 * 4 + Number3 * 3 + Number4 * 2

    remainder = total % 19

    list_of_letters = ['A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B']

    if check_sum_letter == list_of_letters[remainder]:
        return True

carplate = input("What is your registration Number?")
if check_registration_plate(carplate):
    print("Valid")
else:
    print("Invalid")
    

