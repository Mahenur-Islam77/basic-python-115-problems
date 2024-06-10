# 12. Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number among the three
largest = max(num1, num2, num3)

# Print the largest number
print("The largest number is:", largest)
