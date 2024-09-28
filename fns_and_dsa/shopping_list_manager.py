def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("enter the item you want to add: ")
            shopping_list.append(item_name)
            # Prompt for and add an item
            pass
        elif choice == '2':
            item_name = input("enter item you want to remove from list ")
            if item_name not in  shopping_list:
                print("Item not found in a list, please try again ")
            else:
                shopping_list.remove(item_name)
 
            # Prompt for and remove an item
            pass
        elif choice == '3':
            if shopping_list:
                for item in shopping_list:
                    print(f" -{item}")
            else:
                print("the list is empty")
        
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()