task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound (yes/no): ")
match priority :
    case "high" :
        if time == "yes" :
            print(f"Reminder: {task} is a high priority task that requires immeduate attention today!")
        else :
            print(f"Reminder: {task} is a high priority task that requires attention!")
    case "low" :
        print(f"Reminder: {task} is a low priority task. consider completing it when you have free time")