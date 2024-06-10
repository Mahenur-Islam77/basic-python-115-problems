# 31. Print Patterns: Write a Python program using nested loops to print the following pattern:
# *

# **

# ***

# ****

# *****


# Print the pattern using nested loops
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
