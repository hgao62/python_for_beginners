# Chapter 8: Work with Collections - Strings

# #8.1 String
# # A string is a sequence of characters.
# # Strings are written with single or double quotes.
# # Example:
customer_name = "gorge"  # string

# #8.2 String methods
# # String methods are functions that can be called on string objects to perform various operations.
# # Some common string methods include:
# # .upper() - Converts all characters to uppercase.
# # .lower() - Converts all characters to lowercase.
# # .capitalize() - Capitalizes the first character of the string.
# # .title() - Capitalizes the first character of each word in the string.
# # .strip() - Removes leading and trailing whitespace from the string.
# # .replace(old, new) - Replaces all occurrences of old with new in the string.
# # .split(separator) - Splits the string into a list of substrings based on the separator.
# # .inin(iterable) - nns elements of an iterable into a single string, separated by the string.
# # Example:
customer_name = "  gorge  "
customer_name = customer_name.strip()  # remove leading and trailing whitespace
customer_name = customer_name.upper()  # convert to uppercase
customer_name = customer_name.lower()  # convert to lowercase

customer_name = customer_name.capitalize()  # capitalize first character
customer_name = customer_name.title()  # capitalize first character of each word
customer_name = customer_name.replace("gorge", "Gorge")  # replace old with new
customer_name = customer_name.split(" ")  # split string into list of substrings
names = ["Gorge", "Trump", "James"]  # list of names
customer_name = "-".join(names)  # join list of substrings into a single string

print(customer_name)  # output: "Gorge"

# #8.3 String formatting
# # String formatting allows you to insert variables into strings in a readable and efficient way.
# # Python offers several methods for string formatting:
# # Percent % Formatting
# # str.format() Method
# # f-Strings (Formatted String Literals)
# # Example:
name = "Alice"
age = 30
print(
    "My name is %s and I am %d years old." % (name, age)
)  # output: My name is Alice and I am 30 years old.
print(
    "My name is {} and I am {} years old.".format(name, age)
)  # output: My name is Alice and I am 30 years old.

name = "Alice"
age = 30
print(
    f"My name is {name} and I am {age} years old."
)  # output: My name is Alice and I am 30 years old.


first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name  # concatenate strings
print(full_name)  # output: Alice Smith
# #8.4 String slicing
# # String slicing is the process of extracting a substring from a string.
# # It is done using the [start:end] syntax.
# # Example:
customer_name = "Gorge Trump James"
print(customer_name[0:5])  # output: Gorge
print(customer_name[6:11])  # output: Trump
print(customer_name[12:])  # output: James
print(customer_name[:5])  # output: Gorge
print(customer_name[6:])  # output: Trump James
print(customer_name[-5:])  # output: James
print(customer_name[-5:-1])  # output: Jame

reversed_name = customer_name[::-1]  # reverse string
print(reversed_name)  # output: semaJ pmurT egroG

# 8.5 String length
# String length is the number of characters in a string.
customer_name = "Gorge Trump James"
print(len(customer_name))  # output: 17
# 8.6 String membership
# String membership is the process of checking if a substring is present in a string.
customer_name = "Gorge Trump James"
if "Gorge" in customer_name:
    print(
        "The substring is present in the string."
    )  # output: The substring is present in the string.
else:
    print("The substring is not present in the string.")

# 8.7 String iteration
# String iteration is the process of iterating over each character in a string.
customer_name = "Gorge Trump oinames"
for char in customer_name:
    print(char)  # output: G, o, r, g, e, T, r, u, m, p, J, a, m, e, s

# #8.8 String splitting
# # String splitting is the process of splitting a string into a list of substrings.
customer_name = "Gorge Trump James"
split_name = customer_name.split(" ")  # split string into list of substrings
print(split_name)  # output: ['Gorge', 'Trump', 'James']
