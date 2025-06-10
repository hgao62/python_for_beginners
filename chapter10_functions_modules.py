# Chapter 10 # Functions and Modules
# 10.1 How to define a function
# A function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# 1. start with def
# 1.1 followed by the custom name
# 1.2 followed by brackets and parameters(optional)
# 1.3 finally add return statement if need to return something(optional)

import pandas as pd


def add_two_numbers(number_1, number_2):
    result = number_1 + number_2
    return result


def add_two_numbers(number_1, number_2=1000):
    result = number_1 + number_2
    return result


def add_two_numbers_versionb(number_1, number_2=1000):
    result = number_1 + number_2
    return result


res = add_two_numbers_versionb(number_2=500, number_1=100)
print(res)


def add_two_numbers(number_1, number_2):
    res = number_1 + number_2
    return res


def add_two_numbers(number_1, number_2):
    """function to return a value"""
    sum = number_1 + number_2
    return sum


# 10.2 how to call a function
# To call a function, use the function name followed by parentheses.
# You can also pass data into a function by adding parameters inside the parentheses.
# Example:
def add_numbers(a, b):
    return a + b


def save_data_to_csv():
    data = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 30, 35],
            "City": ["New York", "Los Angeles", "Chicago"],
        }
    )
    data.to_csv("c:\\temp\\data.csv")


res = add_numbers(5, 10)
save_data_to_csv(res)


def add_numbers(a, b):
    res = a + b
    return a, res


res1, res2 = add_numbers(5, 10)


# 10.3 Function parameters
# Function parameters are the variables that are defined in the function definition.
# 1. Positional parameters
# 2.  Default parameters
# 3. Keyword arguments


# 10.3.1 Positional parameters
# Positional parameters are the parameters that are passed to a function in the order they are defined.
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 10))  # Output: 15


# 10.3.2 Default parameters
# Default parameters are the parameters that have a default value.
def add_numbers(a, b=10):
    return a + b


print(add_numbers(5))  # Output: 15
print(add_numbers(5, 20))  # Output: 25


# 10.3.3 Keyword arguments
# Keyword arguments are the parameters that are passed to a function using the parameter name.
# This allows you to pass arguments in any order.
def add_numbers(a, b):
    return a + b


print(add_numbers(b=10, a=5))  # Output: 15


# 10.4 positional arguments must be passed before keyword arguments
def add_numbers(a, b=10):
    return a + b


print(add_numbers(5, b=20))  # Output: 25


# 10.4.1 keyword arguments can be passed in any order
def add_numbers(a, b=10):
    return a + b


print(add_numbers(b=20, a=5))  # Output: 25

# 10.5 function return value
# A function can return a value using the return statement.
# The return statement ends the function execution and sends a value back to the caller.
# Example:

# 10.5.0 has no return value


def print_message(message):
    """function to print a message"""
    print(message)


def add_numbers(a, b):
    return a + b


print(add_numbers(5, 10))  # Output: 15


# 10.5.1 return multiple values
def add_and_subtract(a, b):
    return a + b, a - b


res1, res2 = add_and_subtract(10, 5)


# 10.5.2 doesn't return anything
def save_data_to_csv(input_data):
    """function that does something"""
    input_data.to_csv("c:\temp\data.csv")


# 10.6 function scope
# The scope of a variable is the part of the program where the variable is accessible.
# There are two types of scope:
# 1. Local scope
# 2. Global scope
# 10.6.1 Local scope
def my_function():
    x = 10  # Local variable
    print(x)  # Output: 10


my_function()
print(x)  # Error: x is not defined outside the function
# 10.6 .2 Global scope
x = 10  # Global variable


def my_function():
    print(x)  # Output: 10


my_function()
print(x)  # Output: 10


print(x)

# 10.7 Modules: A module is simply a Python file (.py) that contains functions, classes, or variables that you can import and reuse in other files
# 10.7.1 use built-in modules
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793

# 10.7.2 use custom modules
# create a file called utils.py and add the following code:
"""
def calculate_discount(product_name):
   
    if product_name == "A":
        return 0.9
    elif product_name == "B":
        return 0.8
    else:
        return 0.95
"""
from utils import calculate_discount

# now we import this function and use it anywhere in our project to reduce code duplication
print(calculate_discount("A"))  # Output: 0.9

# 10.8  The __name__ == "__main__" Trick

if __name__ == "__main__":
    # This code will only run if the file is run directly
    print("This code runs only when the file is run directly.")
