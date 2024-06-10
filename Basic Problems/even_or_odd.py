# 2. Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.
def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Take input from the user and check validity
try:
    num = int(input("Enter an integer: "))
    check_even_or_odd(num)
except ValueError:
    print("Please enter a valid integer.")
