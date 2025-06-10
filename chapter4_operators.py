# Chapter 4 Operators and Expressions

# 4.1 Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations on numbers.
# They are the most basic operators in programming.
# They are used to perform addition, subtraction, multiplication, division, and modulus operations.
# The following are the arithmetic operators in Python:
# + : addition
# - : subtraction
# * : multiplication
# / : division
# % : modulus

fries_price = 2.5
burger_price = 5.0
combo_price = fries_price + burger_price
print("The combined price of fries and burger is: ", combo_price)

total_budget = 20.0
balance = total_budget - combo_price
print("The remaining balance after buying fries and burger is: ", balance)

price_per_item = 2.0
quantity = 5
total_cost = price_per_item * quantity
print("The total cost of buying 5 items at $2.0 each is: ", total_cost)

total_budget = 20.0
project_number = 2
budgt_per_project = total_budget / project_number
print("The budget for each project is: ", budgt_per_project)

total_oranges = 10
total_people = 3
remainder = total_oranges % total_people
print("The remainder of oranges after distributing them among 3 people is: ", remainder)

# 4.2 Comparison Operators
# Comparison operators are used to compare two values.
# They return a boolean value (True or False) based on the comparison.
# The following are the comparison operators in Python:
# == : equal to
# != : not equal to
# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to

price = 10
print(price == 10)  # True
print(price != 10)  # False
print(price > 5)  # True
print(price < 15)  # True
print(price >= 10)  # True
print(price <= 10)  # Trues

# 4.3 assignment Operators
# Assignment operators are used to assign values to variables.
# They are used to store values in variables.
# The following are the assignment operators in Python:
# = : assignment
# += : add and assign
# -= : subtract and assign
# *= : multiply and assign
# /= : divide and assign
burger_price = 5.0
fries_price = 2.5

burger_price += 1.0  # add 1.0 to burger price, price went up 1 dollar
print("The new burger price is: ", burger_price)  # 6.0

fries_price -= 0.5  # subtract 0.5 from fries price, price went down 0.5 dollar
print("The new fries price is: ", fries_price)  # 2.0

burger_price *= 2  # multiply burger price by 2, price went up 2 times
print("The new burger price is: ", burger_price)  # 12.0

fries_price /= 2  # divide fries price by 2, price went down 2 times
print("The new fries price is: ", fries_price)  # 1.0

# 4.3 Logical Operators
# Logical operators are used to combine multiple conditions.
# They return a boolean value (True or False) based on the conditions.
# The following are the logical operators in Python:
# and : logical AND
# or : logical OR
# not : logical NOT
# Example:
age = 25
is_student = True
is_employee = False
is_eligible = (age >= 18) and (is_student or is_employee)
print("Is the person eligible? ", is_eligible)  # True

balance = 2000
monthly_fee = 14
get_free_money_order = balance >= 1000 or monthly_fee > 5
print("Is the person eligible for free money order? ", get_free_money_order)  # True

lunch_status = False
lunch_status = not lunch_status  # toggle lunch status
print("Is the person having lunch? ", lunch_status)  # True

# 4.4 Membership Operators
# Membership operators are used to check if a value is present in a sequence (list, tuple, string, etc.).
# They return a boolean value (True or False) based on the membership.
# The following are the membership operators in Python:
# in : value is present in the sequence
# not in : value is not present in the sequence
# Example:
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("orange" not in fruits)  # True


# 4.5 Identity Operators
# Identity operators are used to compare the memory location of two objects.
# They return a boolean value (True or False) based on the comparison.
# The following are the identity operators in Python:
# is : is the same object
# is not : is not the same object
# Example:
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(
    f"variable a's memory location id: {id(a)}, b's memory location is: {id(b)}"
)  # memory location of a
print(a is b)  # True
print(f"variable a's memory location id: {id(a)}, b's memory location is: {id(c)}")
print(a is c)  # False
print(a is not c)  # True
