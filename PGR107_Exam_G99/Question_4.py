
# ==============================================================================
# Question 4 (25 points)
# Palindrome checker
# Date: may, 2025
# Author: 21 - 363 - 287 - 41
# ==============================================================================

# ==============================================================================
# This program lets the user check if a chosen string is a palindrome or not
# ==============================================================================

# ==============================================================================
# Checks whether the entered word is a palindrome or not
# ==============================================================================

def checkPalindrome(string):
    return string == string[::-1]


def main():

    while True:
        userInput = input("\nEnter a string you want to check: ").strip().lower()

        # Excludes non alphabetic characters and then converts every character into lowercase
        sanitizedInput = "".join(character.lower() for character in userInput if character.isalpha())

        # Prints out an error-message if the userInput consists of less than 3 characters
        if len(sanitizedInput) < 3:
            print("\nPlease enter a string with at least three letters!")
            continue
    
        # Prints out whether the string is a palindrome or not
        if checkPalindrome(sanitizedInput):
            print(f"\nThe string '{sanitizedInput}' is a palindrome\n")
    
        else:
            print(f"\nThe string '{sanitizedInput}' is not a palindrome\n")

if __name__ == "__main__":
    main()