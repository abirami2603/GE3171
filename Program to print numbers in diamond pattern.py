def print_diamond(n):
    # Print the upper part of the diamond
    for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    # Print the lower part of the diamond
    for i in range(n - 1, 0, -1):
        # Print spaces
        print(" " * (n - i), end="")
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Input: Number of rows in the top half
n = int(input("Enter the number of rows for the diamond pattern: "))

# Display the diamond pattern
if n > 0:
    print_diamond(n)
else:
    print("Please enter a positive integer.")
