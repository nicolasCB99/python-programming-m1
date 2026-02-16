# Global variable used to demonstrate the scope 
program_name = "Simple Calculator"

# Adds the two numbers and returns the result
def add(a, b):
    return a + b

# Subtracts the two numbers with a default value for b
def subtract(a, b=0):
    return a - b

# Divides the two numbers and handles the common errors
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero error")
        return None
    except TypeError:
        print("Invalid input type error")
        return None

# Demonstrating the local vs global scope
def show_program_name():
    local_message = "Running Refrigerator"
    print(local_message, program_name)

# Function calls

print("Add:", add(4, 5))
print()
print("Subtract:", subtract(9))
print()
print("Divide:", safe_divide(27, 3))
print()
print("Divide by zero:", safe_divide(5, 0))
print()
print("Invalid input:", safe_divide(18, "n"))

show_program_name()