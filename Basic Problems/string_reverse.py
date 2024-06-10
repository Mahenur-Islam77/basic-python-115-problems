# 3. String Reverse: Write a Python function to reverse a given string and return the reversed string.

#function to reverse string
def reverse_string(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

# Take input from the user
input_string = input("Enter a string to reverse: ")

# Reverse the input string using the function
reversed_string = reverse_string(input_string)

# Print the original and reversed strings
print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}")