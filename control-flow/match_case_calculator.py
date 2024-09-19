print("Enter the first number")
number1 = int(input())
print("Enter the second number")
number2 = int(input())
print("Choose the operation (+, -, *, /):")

operator = str(input())

match operator :
    case "+" :
        print(f"The result is {number1 + number2}")
    case "-" :
        print(f"The result is {number1 - number2}")
    case "*" :
        print(f"The result is {number1 * number2}")
    case "/" :
        if number2 == 0 :
            print("Cannot divide by zero")
        else :
            print(f"The result is {number1 / number2}")
    case _ :
        print("The operator is invalid")
        