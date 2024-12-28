def list_operations():
    # Initialize an empty list
    my_list = []
    
    while True:
        print("\nChoose an operation:")
        print("1. Add an element")
        print("2. Remove an element")
        print("3. Display the list")
        print("4. Search for an element")
        print("5. Sort the list")
        print("6. Reverse the list")
        print("7. Exit")
        
        choice = int(input("\nEnter your choice (1-7): "))
        
        if choice == 1:
            # Add an element
            element = input("Enter the element to add: ")
            my_list.append(element)
            print(f"{element} added to the list.")
        
        elif choice == 2:
            # Remove an element
            if my_list:
                element = input("Enter the element to remove: ")
                if element in my_list:
                    my_list.remove(element)
                    print(f"{element} removed from the list.")
                else:
                    print(f"{element} not found in the list.")
            else:
                print("The list is empty.")
        
        elif choice == 3:
            # Display the list
            if my_list:
                print("The list elements are:", my_list)
            else:
                print("The list is empty.")
        
        elif choice == 4:
            # Search for an element
            element = input("Enter the element to search for: ")
            if element in my_list:
                print(f"{element} is present in the list at position {my_list.index(element) + 1}.")
            else:
                print(f"{element} is not in the list.")
        elif choice == 5:
             # Sort the list
            my_list.sort()
            print("The list has been sorted:", my_list)
        
        elif choice == 6:
            # Reverse the list
            my_list.reverse()
            print("The list has been reversed:", my_list)
        
        elif choice == 7:
            # Exit
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid operation.")

# Run the program
list_operations()

