# 17. Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.

# Take input for the sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check the type of triangle
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")
