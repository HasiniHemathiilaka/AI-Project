# Program to check whether a word is a palindrome

word = input("Enter a word: ")

if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")