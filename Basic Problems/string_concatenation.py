# 9. String Concatenation: Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.

def concatenate_strings(str1, str2):
    return str1.join(str2)

# Checking Example
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

concatenated_string = concatenate_strings(string1, string2)
print("Concatenated string:", concatenated_string)
