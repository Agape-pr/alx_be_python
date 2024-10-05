def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return False
    except ValueError :
        print("Error: Please enter numeric values only.")
        return False
    else:
        return f"The result of the division is {result}"
        