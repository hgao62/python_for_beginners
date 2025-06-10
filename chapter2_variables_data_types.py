# Chapter2 data types

# 2.1 variables: stored data in memory
variable_name = "value"  # variable name is on left side
# and value is on right side
name = "Alice"
age = 25

# 2.2 Data types: define the type of data
# 2.2.1 Primitive data types(基本数据类型)
# Primitive data types are the most basic data types that are built into a programming language.
# They are the building blocks for more complex data types.
age = 25  # integer
temperature = 98.6  # float
is_true = True  # boolean
name = "alice"  # string
# 2.2.2 Non-primitive data types(非基本数据类型)
# Non-primitive data types are more complex data types that are built using primitive data types.
# They can store multiple values and are more flexible than primitive data types.
customer_names = ["gorge", "trump", "james"]  # list
people_age_map = {"gorge": 24, "trump": 80, "james": 30}  # dictionary
coordinates = (180, 90)  # tuple
unique_id = {1, 2, 3, 4, 5}  # set
# 2.3 Data type conversion
# Data type conversion is the process of converting one data type to another.
# It is also known as type casting.
# In Python, data type conversion is done using built-in functions.
# int() - converts a value to an integer
# float() - converts a value to a float

# str() - converts a value to a string
# list() - converts a value to a list
# tuple() - converts a value to a tuple
# set() - converts a value to a set
# dict() - converts a value to a dictionary
# Example:
age = 25
age_str = str(age)  # convert integer to string
age_float = float(age)  # convert integer to float
age_list = list(age)  # convert integer to list won't work as expected, will raise TypeError
age_tuple = tuple(age_str)  # convert integer to tuple
age_set = set(age_str)  # convert integer to set
# 2.4 Type checking
# Type checking is the process of checking the data type of a value.
# It is also known as type inspection.
# In Python, type checking is done using built-in functions.
# type() - returns the data type of a value
# isinstance() - checks if a value is of a specific data type
# Example:

age = 25
age_type = type(age)  # returns int
is_age_int = isinstance(age, int)  # returns True
is_age_float = isinstance(age, float)  # returns False
