# Basic Calculator Program

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    symbol = "+"
elif operation == "-":
    result = num1 - num2
    symbol = "-"
elif operation == "*":
    result = num1 * num2
    symbol = "*"
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        symbol = "/"
    else:
        result = "undefined (cannot divide by zero)"
        symbol = "/"
else:
    result = "Invalid operation"
    symbol = "?"

# Display the result
print(f"{num1} {symbol} {num2} = {result}")
