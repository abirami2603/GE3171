def find_maximum(L):
    # Initialize the first element as the maximum
    maximum_value = L[0]
    for i in L:
        if i > maximum_value:
            maximum_value = i     
    return maximum_value

# Input the list from the user
L = []
size = int(input('How many elements do you want to enter? '))

if size > 0:
    print('Enter the numbers:')
    for i in range(size):
        try:
            data = int(input())
            L.append(data)
        except ValueError:
            print("Invalid input. Please enter integers only.")
    
    # Call the function and display the result
    max_value = find_maximum(L)
    print("The maximum value in the list is:", max_value)
else:
    print("The list size must be greater than 0.")

