"""Question: Given two dictionaries, merge them into one. If a key exists in both dictionaries, the value from the second dictionary should be kept."""


dictionary1 = {
    "name": "gorge",
    "age": 30,
}

dictionary2 = {
    "city": "New York",
    "age": 31,  # This key exists in both dictionaries
}

for key, value in dictionary2.items():
    # If the key exists in dictionary1, it will be overwritten by the value from dictionary2
    dictionary1[key] = value
