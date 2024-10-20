'''
What is a String?
In Python, a string is a sequence of characters enclosed within quotes. Strings can contain letters, numbers, symbols, and whitespace. 
They are used to handle text-based data in Python programs.
'''

greeting = "Hello, World!"

# 1. create string 
#Strings can be created using single quotes ' ', double quotes " ",
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, World!"

# 2. string indexing ans slicing
#each character in a string has an index, starting from 0 for the first character to -1 for the last character
# 2.1 string indexing
s = "Python"
print(s[0])   # Output: P
print(s[5])   # Output: n
print(s[-1])  # Output: n
print(s[-6])  # Output: P

#2.2 string slicing
#Slicing allows you to obtain a substring by specifying a start and end index. 
# The syntax is string[start:end], where start is inclusive and end is exclusive.
s = "Hello, World!"
print(s[0:5])   # Output: Hello
print(s[7:12])  # Output: World
print(s[:5])    # Output: Hello
print(s[7:])    # Output: World!
print(s[:])     # Output: Hello, World!

#3. string operation
#3.1 concatenation
str1 = "Hello"
str2 = "World"
combined = str1 + ", " + str2 + "!"
print(combined)  # Output: Hello, World!

#3.2 repetition
# Repeat strings using the * operator.
str1 = "Python! "
repeated = str1 * 3
print(repeated)  # Output: Python! Python! Python! 

#3.3 membership testing
#Check if a substring exists within a string using the in and not in operators.
s = "Hello, World!"
print("Hello" in s)      # Output: True
print("Python" not in s) # Output: True

#3.4 common string method
'''
Method	          Description
.upper()	      Converts all characters to uppercase.
.lower()	      Converts all characters to lowercase.
.join(iterable)	  Joins elements of an iterable into a single string, separated by the string.
.find(sub)	      Returns the lowest index of sub if found; otherwise, -1.
.count(sub)	      Returns the number of non-overlapping occurrences of sub.
.split(separator) Splits the string into a list based on separator.
.strip()	      Removes leading and trailing whitespace.
.startswith(prefix)	Checks if the string starts with prefix.
.endswith(suffix)	Checks if the string ends with suffix.
'''

#Examples for functions above
s = "  Hello, World!  "

# Convert to uppercase
print(s.upper())  # Output: "  HELLO, WORLD!  "

# Strip whitespace
print(s.strip())  # Output: "Hello, World!"


# Split
print(s.split(","))  # Output: ['  Hello', ' World!  ']

# Join
words = ['Python', 'is', 'awesome']
print(' '.join(words))  # Output: "Python is awesome"

# Find
print(s.find("World"))  # Output: 8

# Count
print(s.count("o"))  # Output: 2

# Startswith and Endswith
print(s.startswith("  Hello"))  # Output: True
print(s.endswith("!  "))       # Output: True

#4 string formatting
'''
String formatting allows you to insert variables into strings in a readable and efficient way. Python offers several methods for string formatting:

Percent % Formatting
str.format() Method
f-Strings (Formatted String Literals)
'''
#4.1 Percent % Formatting
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Alice and I am 30 years old.

#4.2  str.format() Method
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Bob and I am 25 years old.

#4.3  f-Strings (Formatted String Literals)

name = "Eve"
age = 35
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Eve and I am 35 years old.
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")
# Output: The sum of 5 and 10 is 15.

#5 escape characters
'''

Escape Sequence	Description
\'	 Single quote
\"	Double quote
\\	Backslash
\n	Newline
\t	Horizontal tab
\r	Carriage return
\b	Backspace
\f	Form feed
\v	Vertical tab
'''
# Including quotes inside strings
print('It\'s a beautiful day!')  # Output: It's a beautiful day!
print("He said, \"Hello!\"")     # Output: He said, "Hello!"

# Newline and tab
print("First Line\nSecond Line")
# Output:
# First Line
# Second Line

print("Column1\tColumn2")
# Output:
# Column1    Column2

# 6 raw string

# Raw strings treat backslashes (\) as literal characters and do not interpret them as escape characters. They are prefixed with r or R.
# Regular string with escape character
print("C:\\Users\\Alice\\Documents")
# Output: C:\Users\Alice\Documents

# Raw string
print(r"C:\\Users\Alice\Documents")
# Output: C:\Users\Alice\Documents


# 6 strings are immutable
s = "Hello"
s[0] = "h"  # This will raise a TypeError



f"{be}"