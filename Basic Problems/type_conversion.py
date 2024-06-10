# 4. Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.

def convert_list_to_strings(int_list):
    return [str(element) for element in int_list]

# Take input from the user
input_string = input("Enter a list of integers separated by spaces: ")

# Split the input string into individual strings representing numbers
input_list = input_string.split()

# Convert the list of strings to a list of integers
integer_list = [int(element) for element in input_list]

# Convert the list of integers to a list of strings
string_list = convert_list_to_strings(integer_list)

print(f"Original list of integers: {integer_list}")
print(f"Converted list of strings: {string_list}")