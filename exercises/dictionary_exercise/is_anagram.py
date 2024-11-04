'''
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

''' 
# s_dict = {'r':2, 'a':2, 'c':2,'e':1}
# t_dict = {'r':2, 'a':2,'c':2, 'e':1}


def is_anagram( s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    for letter in s:
        if letter not in s_dict:
            s_dict[letter] =1
        else:          
            s_dict[letter] = s_dict[letter] +1
            
    for letter in t:
        # if key does not exist
        if letter not in t_dict:
            t_dict[letter] =1
        # else if key exist 
        else:          
            t_dict[letter] = t_dict[letter] +1
            
    
    return s_dict == t_dict
    
def is_anagram(s: str, t: str) -> bool:
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    return s_sorted == t_sorted
s = "racecar"
t = "carrace"
print(is_anagram(s,t))
