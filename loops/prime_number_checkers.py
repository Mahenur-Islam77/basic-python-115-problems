# 27. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

# Take input from the user
N = int(input("Enter an integer: "))

# Prime number check function
def is_prime(N):
    # Handle edge cases
    if N <= 1:
        return False
    if N == 2:
        return True

    # Initialize the divisor
    divisor = 2
    
    # Check for factors up to the square root of N
    while divisor * divisor <= N:
        if N % divisor == 0:
            return False
        divisor += 1

    return True

# Check if the number is prime and print the result
if is_prime(N):
    print(f"{N} is a prime number.")
else:
    print(f"{N} is not a prime number.")
