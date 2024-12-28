# Program to exchange the values of two variables
def exchange_values():
    # Taking input for two variables
    x = input("Enter the value of x: ")
    y = input("Enter the value of y: ")
    
    print(f"\nBefore swapping: x = {x}, y = {y}")
    
    # Swapping values
    x, y = y, x
    
    print(f"After swapping: x = {x}, y = {y}")

# Call the function
if __name__ == "__main__":
    exchange_values()

