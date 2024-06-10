# 18. Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.

import cmath

# Take input for the coefficients of the quadratic equation
a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))
c = float(input("Enter the coefficient 'c': "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of the roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print("The roots are real and distinct.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    # Two real and equal roots
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root:", root)
else:
    # Complex roots
    real_part = -b / (2*a)
    imag_part = cmath.sqrt(abs(discriminant)) / (2*a)
    print("The roots are complex.")
    print("Root 1:", real_part, "+", imag_part, "i")
    print("Root 2:", real_part, "-", imag_part, "i")
