def divide(a, b):
    """Performs division of two numbers."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

if __name__ == "__main__":
    print("Division Operation")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = divide(num1, num2)
    print(f"Result: {result}")
