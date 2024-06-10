# 25. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.


# Take input from the user
N = int(input("Enter a positive integer: "))

# Initialize variables
sum_of_even = 0
number = 2  # Starting from 2 as 1 is not even

# Calculate the sum of even numbers using a while loop
while number <= N:
    sum_of_even += number
    number += 2  # Increment by 2 to get the next even number

# Print the sum of even numbers
print("Sum of even numbers between 1 and", N, "is:", sum_of_even)
