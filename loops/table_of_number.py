# 22. Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.

# Take input from the user
N = int(input("Enter a number to generate its multiplication table: "))

# Print the multiplication table using a for loop
print(f"Multiplication table of {N}:")
for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")
