# 36. List Max and Min: Write a Python program to find the maximum and minimum values in a given list of integers.

# Define the list of integers
numbers = [int(x) for x in input("Enter the list of integers separated by space: ").split()]

# Find the maximum and minimum values in the list
list_max = max(numbers)
list_min = min(numbers)

# Print the maximum and minimum values
print("The maximum value in the list is:", list_max)
print("The minimum value in the list is:", list_min)
