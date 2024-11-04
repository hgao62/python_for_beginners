
'''
please finish function find vowels below to find the number of vowels in input string

Vowels are follow letter below, you can copy this variable to your code directly
vowels = "aeiou"

'''



def find_vowels(s:str) -> int:
    count = 0
    for letter in s:
        if letter.lower() in 'aeiou':
            count = count +1
    return count
            



my_str = "All animals are equal. Some are more equal"
print(find_vowels(my_str))
### test cases below ####

assert find_vowels(my_str)==18
