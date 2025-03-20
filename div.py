def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    """Performs division of two numbers."""
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2
