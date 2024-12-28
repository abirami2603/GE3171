# Creating Dictionary
college = {
    "name": "NSCET",
    "code": "INDIA",
    "id": "9210"
}
print(college)

# Adding new element
college["location"] = "IBP"
print(college)

# Changing element
college["location"] = "Theni"
print(college)

# Accessing elements in dictionary
print(college.get('name'))

# Removing elements from a dictionary
college.pop("code")
print(college)

# Length of dictionary
print(len(college))

# Get all the keys in the dictionary
print(college.keys())

# For loop in dictionary
squares = {}
for x in range(6):
    squares[x] = x * x
print(squares)

# Equivalent code using dictionary comprehension
squares = {x: x * x for x in range(6)}
print(squares)

# Dictionary operations with if conditionals
odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
print(odd_squares)

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)
print(2 not in squares)

# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

# Print sorted elements
print(sorted(squares.keys()))  # Sorted keys instead of dictionary itself

