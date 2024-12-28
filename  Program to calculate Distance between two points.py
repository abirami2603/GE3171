import math

def calculate_distance(x1, y1, x2, y2):
    # Calculate the distance using the distance formula
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Input coordinates for the two points
print("Enter the coordinates of the first point:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("\nEnter the coordinates of the second point:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Calculate and display the distance
distance = calculate_distance(x1, y1, x2, y2)
print(f"\nThe distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
