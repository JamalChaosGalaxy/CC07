def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()
    
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return "Yes"
    else:
        return "No"

# Test the function
word = input("Enter a word: ")
print(is_palindrome(word))

