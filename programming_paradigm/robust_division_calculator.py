def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return False
    except ValueError :
        print("Erroe: Plase enter numeric values only")
        return False
    else:
        return result
        