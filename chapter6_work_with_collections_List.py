# Chapter 6: Work with Collections -List
# 6.1 list
# # A list is a collection of items that are ordered and changeable.
# # Lists are written with square brackets.
# # Example:
customer_names = ["gorge", "trump", "james"]  # list

# 6.2 Modify element in list
customer_names[0] = "gorge"  # modify first element
customer_names[1] = customer_names[1].upper()  # modify second element

# 6.3 Add elements to the list
customer_names.append("james")  # add element to the end of the list
customer_names.insert(2, "james")  # add element to the index 2

# 6.4 Remove elements from list
customer_names.pop()  # remove last element
customer_names.pop(1)  # remove second element
customer_names.remove("james")  # remove element by value
# 6.5 Index slicing
customer_names = ["gorge", "trump", "james"]
print(customer_names[0:2])  # output: ['gorge', 'trump']
# 6.6 Index slicing Get first n elements from list
print(customer_names[:2])  # output: ['gorge', 'trump']
# 6.7 Sort a list
#  Sort in place
customer_names.sort()  # sort the list in place
customer_names.sort(reverse=True)  # sort the list in reverse order
# Sort to return a new list
sorted_customer_names = sorted(customer_names)  # sort the list and return a new list

# 6.8 List comprehension(Common Interview Question!)
# List comprehension is a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses.
# List comprehension is more compact and faster than the traditional for loop.
# Example:
makeup_prices = [100, 120, 130, 140, 150]  # 30% off
discount_prices = []  # create an empty list
for price in makeup_prices:
    discount_prices.append(price * 0.7)  # add 30% off price to the list

discount_prices = [price * 0.7 for price in makeup_prices]  # list comprehension

print(discount_prices)  # output: [70.0, 84.0, 91.0, 98.0, 105.0]
# 6.9 Nested list
# A nested list is a list that contains other lists.
# Example:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])  # output: [1, 2, 3]
print(nested_list[0][1])  # output: 2
