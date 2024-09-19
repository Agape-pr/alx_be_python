number1 = int(input("enter the first number"))
number2 = int(input("enter the second number"))
operator = str(input("Choose the operation (+, -, *, /):"))

match operator :
    case "+" :
        print(f"the result is {number1 + number2}")
    case "-" :
        print(f"the result is {number1 - number2}")
    case "*" :
        print(f"the result is {number1 * number2}")
    case "/" :
        if number2 == 0 :
            print("Cannot divide by zero")
        else :
            print(f"the result is {number1 / number2}")
    case _ :
        print("the operator is invalid")
        