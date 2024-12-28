def print_pyramid(n):
    # Loop through each row
    for i in range(1, n + 1):
        # Print spaces to align numbers in a pyramid shape
        print(" " * (n - i), end="")
        # Print numbers in the current row
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Move to the next line

# Input: Number of rows for the pyramid
n = int(input("Enter the number of rows for the pyramid pattern: "))

# Display the pyramid pattern
if n > 0:
    print_pyramid(n)
else:
    print("Please enter a positive integer.")
