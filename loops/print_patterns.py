# 26. Print Patterns: Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.

# Right-Angled Triangle
print("Right-Angled Triangle:")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# Inverted Right-Angled Triangle
print("\nInverted Right-Angled Triangle:")
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

# Equilateral Triangle
print("\nEquilateral Triangle:")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Square
print("\nSquare:")
side = 5
for i in range(side):
    print("*" * side)

# Hollow Square
print("\nHollow Square:")
side = 5
for i in range(side):
    if i == 0 or i == side - 1:
        print("*" * side)
    else:
        print("*" + " " * (side - 2) + "*")
