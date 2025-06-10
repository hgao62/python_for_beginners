# Chapter 9: Work with Collections - Sets

# #9.1 Set
# # A set is a collection of unique elements.
# # Sets are unordered, meaning the elements do not have a specific order.
# # Sets are mutable, meaning you can add or remove elements after creation.
# # Sets are written with curly brackets or the set() function.
# # Example:
my_set = {1, 2, 3, 4, 5}  # Creating a set using curly braces
print(my_set)  # output: {1, 2, 3, 4, 5}
another_set = set([1, 2, 2, 3, 4])  # Creating a set using the set() function
print(another_set)  # output: {1, 2, 3, 4}

# 9.2 Set Characteristics
# 9.2.1 Unordered
s = {3, 1, 4, 2}
print(s)  # The output order may be different each time
# 9.2.2 Unique Elements
s = {1, 2, 2, 3, 4, 4, 5}
print(s)  # output: {1, 2, 3, 4, 5}  (duplicates removed)
# 9.2.3 Mutable
s = {1, 2, 3}
s.add(4)  # Adding an element
s.remove(2)  # Removing an element
s.discard(3)  # Removing an element (no error if not found)
s.clear()  # Removing all elements


# 9.3 Set Operations
# 9.3.1 Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)  # Union of two sets
print(set3)  # output: {1, 2, 3, 4, 5}
set3 = set1 | set2  # Union using the | operator
print(set3)  # output: {1, 2, 3, 4, 5}
# 9.3.2 Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)  # Intersection of two sets
print(set3)  # output: {3}
set3 = set1 & set2  # Intersection using the & operator
print(set3)  # output: {3}
# 9.3.3 Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.difference(set2)  # Difference of two sets
print(set3)  # output: {1, 2}
set3 = set1 - set2  # Difference using the - operator
print(set3)  # output: {1, 2}

# 9.3.4 Copying a Set
set1 = {1, 2, 3}
set2 = set1.copy()  # Copying a set

# 9.3.5 Set Comprehension
# Set comprehension is a concise way to create sets.
set_comprehension = {
    x for x in range(10) if x % 2 == 0
}  # Creating a set using set comprehension
print(set_comprehension)  # output: {0, 2, 4, 6, 8}

# 9.4 iterating through a set
# You can iterate through a set using a for loop.
for item in my_set:
    print(item)  # output: 1, 2, 3, 4, 5 (order may vary)


""" Exercise: Duplicate Integer
Duplicate Integer
Given an integer array nums, please complete has_duplicate function below so that it return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""


nums = [1, 2, 3, 3]  # return True
nums = [1, 2, 3, 4]  # return False
empty_set = set()  # use set other than list:
has_duplicate = False
for num in nums:
    if num in empty_set:
        has_duplicate = True
        break
    empty_set.add(num)

print(has_duplicate)  # output: True
