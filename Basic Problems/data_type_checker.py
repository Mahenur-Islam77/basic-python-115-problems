# 6. Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.)

def get_data_type(variable):
    return type(variable).__name__

# Example usage
user_input = input("Enter a value: ")

# Try to interpret the user input as different types
try:
    # Try to convert to int
    int_value = int(user_input)
    dataType = get_data_type(int_value)
except ValueError:
    try:
        # Try to convert to float
        float_value = float(user_input)
        dataType = get_data_type(float_value)
    except ValueError:
        # If conversion to int and float fails, consider it as a string
        dataType = get_data_type(user_input)

print(f"The data type of '{user_input}' is: {dataType}")
