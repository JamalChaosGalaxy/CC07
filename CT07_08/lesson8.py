# isdigit = checks if all the characters in a varibale are numbers
# isalpha = check if all the characters in a variable are 
# isalnum = only nums and alphabet letters and not special character
# isupper = checks if the letters are uppercase
# islower = checks if the letters are lowercase
# and, or , not


# while True:
#     password = input("Please input your password: ")
#     if len(password) >= 8 and password.isupper == False and password.islower == False and password.isalpha == False and password.isdigit == False and password.isalnum == True:
#         print("Password is valid")
#         break
#     else:
#         print("Password is invalid")

# is8_char_long = False
# has_upper = False
# has_lower = False
# has_num = False
# only_alnum = False

password = input("Please enter your password: ")
has_upper = not(password.islower())
has_lower = not(password.isupper())
has_num = not(password.isalpha())
has_alpha = not(password.isalnum())

if (password.isalnum() and len(password) >= 8 and has_upper and has_lower and has_num):
    print("Password valid")
else:
    print("Password invalid")

# sentence = input("What is your sentence?")
# mocked_sentence = ""
# upper = True
# lower = False

# for char in sentence:
#     if upper == True:
#         mocked_sentence += char.lower()
#         upper = False
#     if lower == True:
#         mocked_sentence += char.upper()
#         upper = True
        
# print(mocked_sentence)

# password = "hello world"
# print(password.split(","))

# print(password.join(" "))

word = "Hello World"
oval = word.split(" ")
sentence = []

for word in oval:
    sentence.append(word[::-1])
sentence = " ".join(sentence)
print(sentence)
    


# print("burgers"[::-1])

# word = "mom"

# is_palindrome = word == word[::-1]
# print(word[::-1])
# print(f"Output: ",is_palindrome)



# word = input("Input: ")

# is_palindrome = word == word[::-1]
# print(f"Output: ",is_palindrome)



# while True:
#     word = input("Input: ")

#     if (word == "end"):
#         break

#     is_palindrome = word == word[::-1]
#     print(f"Output: ",is_palindrome)




# NumOfPalindrome = 0
# ListOfPalindrome = []

# for word in list:
#     is_palindrome = word == word[::-1]
#     if(is_palindrome):
#         NumOfPalindrome += 1
#         ListOfPalindrome.append(word)

# print(NumOfPalindrome)
# print(ListOfPalindrome)

# for word in ListOfPalindrome:
#     print(word)


# sales_data = [
#     ["Apple", 50, 1.99],
#     ["Banana", 45, 0.99],
#     ["Orange", 30, 2.49],
#     ["Grapefruit", 25, 3.99],
#     ["Mango", 20, 2.99],
# ]

# earned = []
# for fruits in sales_data:
#     fruit, sold, price = fruits
#     earned.append(sold * price)


# top_fruits = []
# max_value = 0
# for price in earned:
#     max_value = price
#     if(max_value < price):
#         max_value = price

# print(max_value)

# for fruits in sales_data:
#     fruit_Max = fruits[earned.index(max_value)]

# print(fruit_Max)

# data = []
# skibidi = []

# while True:
#     code = input("Enter 'a' to add, 's' to search, 'd' to display, or 'q' to quit: ")
#     if code == "q": 
#         break
#     if code == "a":
#         for skibidi in data:
#             for skidata in skibidi:
#                 name, password, url = skidata
#         name = input("Enter Username: ")
#         word = input("Enter Password: ")
#         Url = input("Enter Website Url: ")
#     if code == "s":
#         search = input("Enter search keyword: ")
#         for skidata in skibidi:
#             if search == skidata:
#                 print(skibidi)
#     if code == "d":
#         print(skibidi)