"""Finish function drop_digits below so that it remove numbers 1- 10 from input string"""


my_str = "He12llo, Py00th55on!"  # output should be"Hello, Python!"
new_string_list = []
for letter in my_str:
    if not letter.isnumeric():
        new_string_list.append(letter)

print("".join(new_string_list))
