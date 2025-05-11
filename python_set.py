#1. Creating a set
# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# Creating a set using the set() function
another_set = set([1, 2, 2, 3, 4])
print(another_set)  # {1, 2, 3, 4}

# Creating an empty set
empty_set = set()  # Note: {} creates an empty dictionary
print(type(empty_set))  # <class 'set'>

#2.  Set Characteristics

#2.1 unordered
s = {3, 1, 4, 2}
print(s)  # The output order may be different each time

#2.2 unique elements
s = {1, 2, 2, 3, 4, 4, 5}
print(s)  # {1, 2, 3, 4, 5}  (duplicates removed)
