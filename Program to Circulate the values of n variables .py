def circulate_values():
    # Input the number of variables
    n = int(input("Enter the number of variables: "))
    
    # Input the values of the variables
    values = []
    for i in range(n):
        value = input(f"Enter value {i + 1}: ")
        values.append(value)
    
    print(f"\nBefore circulation: {values}")
    
    # Perform circulation
    values = values[-1:] + values[:-1]
    
    print(f"After circulation: {values}")

# Call the function
if __name__ == "__main__":
    circulate_values()
