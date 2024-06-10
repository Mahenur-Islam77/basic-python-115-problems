# 29. Reverse String: Write a Python program using a while loop to reverse a given string.

# Take input from the user
original_string = input("Enter a string: ")

# Initialize variables
reversed_string = ""
index = len(original_string) - 1

# Reverse the string using a while loop
while index >= 0:
    reversed_string += original_string[index]
    index -= 1

# Print the reversed string
print("Reversed string:", reversed_string)