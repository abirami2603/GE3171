def fibonacci_sequence(n):
    # Initialize the first two terms
    a, b = 0, 1
    sequence = []
    
    # Generate Fibonacci sequence
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Validate input
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Get and display the Fibonacci sequence
    result = fibonacci_sequence(n)
    print(f"The Fibonacci sequence up to {n} terms is: {result}")
