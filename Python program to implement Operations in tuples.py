def tuple_operations():
    # Initialize a tuple
    my_tuple = ()
    
    while True:
        print("\nChoose an operation:")
        print("1. Add elements to a tuple")
        print("2. Access an element")
        print("3. Find length of the tuple")
        print("4. Search for an element")
        print("5. Concatenate two tuples")
        print("6. Iterate through the tuple")
        print("7. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-7): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue
        
        if choice == 1:
            # Add elements (tuples are immutable, so create a new tuple)
            elements = input("Enter elements separated by space: ").split()
            my_tuple += tuple(elements)
            print("Updated tuple:", my_tuple)
        
        elif choice == 2:
            # Access an element
            if my_tuple:
                try:
                    index = int(input("Enter the index to access (0-based): "))
                    print(f"Element at index {index} is {my_tuple[index]}")
                except (ValueError, IndexError):
                    print("Invalid index. Please enter a valid index within range.")
            else:
                print("The tuple is empty.")
        
        elif choice == 3:
            # Find the length of the tuple
            print("The length of the tuple is:", len(my_tuple))
        
        elif choice == 4:
            # Search for an element
            element = input("Enter the element to search for: ")
            if element in my_tuple:
                print(f"{element} is present in the tuple at position {my_tuple.index(element) + 1}.")
            else:
                print(f"{element} is not in the tuple.")
        
        elif choice == 5:
            # Concatenate two tuples
            new_elements = input("Enter elements of another tuple separated by space: ").split()
            new_tuple = tuple(new_elements)
            my_tuple += new_tuple
            print("Concatenated tuple:", my_tuple)
        
        elif choice == 6:
            # Iterate through the tuple
            if my_tuple:
                print("Tuple elements are:")
                for element in my_tuple:
                    print(element, end=" ")
                print()
            else:
                print("The tuple is empty.")
        
        elif choice == 7:
            # Exit
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid operation.")
            
# Run the program
tuple_operations()

