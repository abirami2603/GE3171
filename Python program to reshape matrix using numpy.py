import numpy as np

# Initialize a 2D numpy array
a = np.array([(8, 9, 10), (11, 12, 13)])
print("Original Array:")
print(a)

try:
    # Attempt to reshape the array
    a = a.reshape(3, 2)
    print("\nReshaped Array (3x2):")
    print(a)
except ValueError:
    print("\nError: The reshaping dimensions are incompatible with the original array.")
