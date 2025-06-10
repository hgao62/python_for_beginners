# Chapter 7: Work with Collections - Dictionary

# #7.1 Dictionary
# # A dictionary is a collection of key-value pairs.
# # Dictionaries are written with curly brackets.
# # Example:
customer_info = {
    "name": "gorge",
    "age": 30,
}

# 7.2 access values
# Accessing values
# You can access the values in a dictionary by using the keys.
print(customer_info["name"])  # output: gorge
print(customer_info["age"])  # output: 30
# 7.3 Adding or Modifying Key-Value Pairs
# Adding new key-value pair
customer_info["city"] = "New York"  # Adding new key-value pair
# Updating an existing key
customer_info["age"] = 31  # Updating an existing key

# 7.4 Removing Key-Value Pairs
# Using pop()
age = customer_info.pop("age")  # Removes 'age' and returns '31'
# Using del
del customer_info["city"]  # Removes the 'city' key-value pair
# Using popitem()
last_item = customer_info.popitem()  # Removes the last inserted key-value pair

# 7.5 Looping all key-value pairs in a dictionary
# Iterating through keys
for key in customer_info.keys():
    print(key)  # output: name
# Iterating through values
for value in customer_info.values():
    print(value)  # output: gorge
# Iterating through key-value pairs
for key, value in customer_info.items():
    print(f"{key}: {value}")  # output: name: gorge

# 7.6 Checking if a key exists
key_to_check = "name"
if key_to_check in customer_info:
    print(
        f"{key_to_check} exists in the dictionary."
    )  # output: name exists in the dictionary.
