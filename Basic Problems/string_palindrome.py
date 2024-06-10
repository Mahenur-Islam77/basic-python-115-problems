# 7. String Palindrome: Write a Python function to check if a given string is a palindrome or not.

def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    clean_string = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return clean_string == clean_string[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
