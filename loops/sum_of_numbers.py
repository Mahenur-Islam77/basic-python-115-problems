# 20. Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.

# Take input from the user
N = int(input("Enter a positive integer: "))

# Initialize the sum
sum_of_numbers = 0

# Calculate the sum of the first N natural numbers using a for loop
for i in range(1, N + 1):
    sum_of_numbers += i

# Print the sum of the first N natural numbers
print("Sum of the first", N, "natural numbers is:", sum_of_numbers)
