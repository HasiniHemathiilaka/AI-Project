# Palindrome Checker

# Ask the user for a word
word = input("Enter a word: ")

# Convert to lowercase so "Madam" and "madam" are treated the same
word = word.lower()

# Reverse the word using slicing
reversed_word = word[::-1]

# Compare the original with the reversed version
if word == reversed_word:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")