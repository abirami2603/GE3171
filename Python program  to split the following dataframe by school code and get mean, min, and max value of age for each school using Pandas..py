import pandas as pd

# Set display options
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

# Creating the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'V', 'VI', 'V'],
    'name': ['Albert Franco', 'Gino Mcnaill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcnaill', 'DavidParkes'],
    'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['Street1', 'Street2', 'Street3', 'Street1', 'Street2', 'Street4']
}, index=['s1', 's2', 's3', 's4', 's5', 's6'])

# Display the original DataFrame
print("Original DataFrame:")
print(student_data)

# Group by school_code and calculate mean, min, and max age
print("\n Mean, Min, and Max value of age for each value of the school:")
grouped_single = student_data.groupby('school_code').agg({'age': ['mean', 'min', 'max']})
print(grouped_single)

