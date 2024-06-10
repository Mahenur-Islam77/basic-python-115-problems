# 19. Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

# Take input from the user
number = int(input("Enter a number: "))

# Check the range of the number and print the corresponding message
if number >= 0 and number <= 50:
    print("The number falls within the range 0-50.")
elif number >= 51 and number <= 100:
    print("The number falls within the range 51-100.")
elif number >= 101 and number <= 150:
    print("The number falls within the range 101-150.")
else:
    print("The number is above 150.")
