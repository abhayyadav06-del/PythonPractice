try:
    numerator = float(input("Enter first the value:"))
    denominator = float(input("Enter second number:"))
    result = numerator / denominator
    print(f"result : {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid numeric values.")
