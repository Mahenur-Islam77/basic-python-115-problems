# 33. Chessboard Pattern: Write a Python program using nested loops to print a chessboard pattern (alternating “X” and “O” characters) of size 8×8.34. 

# Chessboard Pattern
print("Chessboard Pattern:")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  # Move to the next line after printing each row
