def area(r):
    # Calculate the area of the circle
    result = 3.14 * r * r
    return result

# Input: Radius of the circle
try:
    radius = float(input("Enter the radius: "))
    if radius < 0:
        print("Radius cannot be negative. Please enter a positive value.")
    else:
        # Compute area
        a = area(radius)
        # Print the result with proper formatting
        print("The area of the circle with radius %.2f is: %.2f" % (radius, a))
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
