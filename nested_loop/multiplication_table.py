# 30. Multiplication Table: Write a Python program using nested loops to print the multiplication table from 1 to 10.

# Print the multiplication table using nested loops
print("Multiplication Table:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} × {j} = {i * j}")
    print()  # Move to the next line after printing each table
