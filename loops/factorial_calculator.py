# 21. Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.

# Take input from the user
N = int(input("Enter a non-negative integer: "))

# Initialize the result to 1 (as factorial of 0 is 1)
factorial = 1

# Ensure the input is a non-negative integer
if N < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Use  while loop to calculate the factorial
    while N > 0:
        factorial *= N  
        N -= 1  

    # Print the factorial
    print(f"The factorial of the given number is: {factorial}")
