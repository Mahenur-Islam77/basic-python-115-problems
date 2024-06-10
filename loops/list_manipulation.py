# 28. List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.

# Take input from the user
input_list = input("Enter a list of integers separated by spaces: ")

# Convert the input string to a list of integers
integer_list = list(map(int, input_list.split()))

# Initialize variables
sum_of_elements = 0
max_value = integer_list[0]
min_value = integer_list[0]

# Calculate sum, max, and min using a for loop
for num in integer_list:
    sum_of_elements += num
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

# Calculate the average
average = sum_of_elements / len(integer_list)

# Print the results
print(f"Sum: {sum_of_elements}")
print(f"Average: {average}")
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
