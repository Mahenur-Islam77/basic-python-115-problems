# 35. List Average: Write a Python program to calculate the average of all elements in a given list of integers
# Define the list of integers
numbers = [int(x) for x in input("Enter the list of integers separated by space: ").split()]

# Calculate the average of all elements in the list
list_average = sum(numbers) / len(numbers)

# Print the average of all elements
print("The average of all elements in the list is:", list_average)
