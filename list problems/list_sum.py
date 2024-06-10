# 34. List Sum: Write a Python program to find the sum of all elements in a given list of integers.

# Define the list of integers
numbers = [int(x) for x in input("Enter the list of integers separated by space: ").split()]

# Calculate the sum of all elements in the list
list_sum = sum(numbers)

# Print the sum of all elements
print("The sum of all elements in the list is:", list_sum)
