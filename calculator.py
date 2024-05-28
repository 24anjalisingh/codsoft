# Simple Calculator Program in Python

# Function definitions for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Displaying the operation options to the user
print("Choose an operation:\n" \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n")


# Getting the user's choice
choice = int(input("Enter the number corresponding to your choice (1, 2, 3, 4): "))

# Getting the numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing the chosen operation and displaying the result
if choice == 1:
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == 2:
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == 3:
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == 4:
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid selection")


    
