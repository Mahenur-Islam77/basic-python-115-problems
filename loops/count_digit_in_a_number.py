# 23. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.

# Take input from the user
N = int(input("Enter an integer: "))

# Initialize the digit count
count = 0

# Handle negative numbers by taking the absolute value
N = abs(N)

# Special case for 0, as it has 1 digit
if N == 0:
    count = 1
else:
    # Using while loop to count the digits
    while N > 0:
        N //= 10  
        count += 1  

# Print the number of digits
print(f"The number of digits in the given integer is: {count}")
