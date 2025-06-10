"""
please finish function find vowels below to find the number of vowels in input string

Vowels are follow letter below, you can copy this variable to your code directly
vowels = "aeiou"

"""


my_str = "All animals are equal. Some are more equal"  # should output 18
count = 0
for letter in my_str:
    if letter.lower() in "aeiou":
        count = count + 1

print(count)  # output: 18
