# 8. String Reversal with Slicing: Write a Python function to reverse a given string using slicing.

def reverse_string(s):
    return s[::-1]

# Take input from the user
input_string = input("Enter a string: ")

# Reverse the string using the reverse_string function
reversed_string = reverse_string(input_string)

# Print the reversed string
print("Reversed string:", reversed_string)
