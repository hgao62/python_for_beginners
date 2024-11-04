'''Finish function drop_digits below so that it remove numbers 1- 10 from input string'''

def drop_digits(s:str) -> str:
    new_string_list = []

    for letter in s:
        if not letter.isnumeric():
            new_string_list.append(letter)
    
    return ''.join(new_string_list)



my_str = 'He12llo, Py00th55on!'
assert drop_digits(my_str)=="Hello, Python!"
