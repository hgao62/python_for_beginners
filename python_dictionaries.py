'''
A dictionary in Python is an unordered collection of key-value pairs. Each key is unique, and the key-value pairs are separated by a colon (:). Dictionaries are mutable, meaning you can modify them after creation.
'''
# 1. create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

#2. access values
# Accessing values


#2.1 If you try to access a key that doesn't exist, Python will raise a KeyError. 
# To avoid this, use the get() method, which returns None or a default value if the key isn't found.
print(person.get('name'))       # Output: Alice
print(person.get('job', 'N/A')) # Output: N/A


# 3. Adding or Modifying Key-Value Pairs
person['first_name'] = 'John junior'  # Adding new key-value pair
person['age'] = 26          # Updating an existing key

# 4. Removing Key-Value Pairs
# Using pop()
age = person.pop('age')  # Removes 'job' and returns 'Engineer'
print(person)            # {'name': 'Alice', 'age': 26, 'city': 'Toronto'}

# Using del
del person['first_name']        # Removes the 'city' key-value pair
print(person)             # {'name': 'Alice', 'age': 26}

# Using popitem()
last_item = person.popitem()
print(last_item)          # ('age', 26)


#5 Looping all key-value pairs in a dictionary

# Iterating through keys
for key in person.keys():
    print(key)

person.items()
# Iterating through values
for value in person.values():
    print(value)

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")


stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}


selected_stocks = {'AMZN':3380}

stocks.pop("AAPL")

selected_stocks = {}
for symbol, price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price

selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}

print(selected_stocks)