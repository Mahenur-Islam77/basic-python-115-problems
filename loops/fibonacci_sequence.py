# 24. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.

# Take input from the user
N = int(input("Enter a positive integer for the Fibonacci sequence limit: "))

# Initialize the first two numbers in the Fibonacci sequence
a, b = 0, 1

# List to store the Fibonacci sequence
fibonacci_sequence = []

# Generate the Fibonacci sequence up to the limit N
for _ in range(N):
    fibonacci_sequence.append(a)
    a, b = b, a + b

# Print the Fibonacci sequence
print("Fibonacci sequence up to the limit:", fibonacci_sequence)
