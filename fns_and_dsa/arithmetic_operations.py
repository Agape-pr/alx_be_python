def perform_operation(num1, num2, operation):
    if operation == "add" :
        return num1 + num2 
    elif operation == "substraction" :
        return num1-num2 
    elif operation == "multiply" :
        return num1 * num2
    elif operation == "divide" :
        if num2 == 0 :
            print("you can nit devide with zero")
        else :
            return num1 / num2 
    