# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

# Take input from the user
hour = int(input("Enter the time in hours (24-hour format): "))

# Check the time and print the corresponding greeting
if hour >= 0 and hour < 12:
    print("Good Morning!")
elif hour >= 12 and hour < 18:
    print("Good Afternoon!")
elif hour >= 18 and hour < 24:
    print("Good Evening!")
else:
    print("Good Night!")
