Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_bound = input("Is it time-bound (yes/no): ")
match Priority :
    case "high" :
        if Time_bound== "yes" :
            print(f"Reminder: {Task} is a high {Priority} task that requires immeduate attention today!")
        else :
            print(f"Reminder: {Task} is a high {Priority} task that requires attention!")
    case "medium" :
        print(f"Reminder: {Task} is a {Priority} that requires immediate attention today!")
    case "low" :
        print(f"Reminder: {Task} is a {Priority} priority task. consider completing it when you have free time")