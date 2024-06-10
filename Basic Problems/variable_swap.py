# 1. Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable.

# Function to swap values
def swap(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    
    # Swap without using a temporary variable
    a, b = b, a
    
    print(f"After swap: a = {a}, b = {b}")
    return a, b

# Checking Example:
x = 5
y = 10

x, y = swap(x, y)