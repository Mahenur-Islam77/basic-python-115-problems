# 11. Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

# Take input from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero and print the corresponding message
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
