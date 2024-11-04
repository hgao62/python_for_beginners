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
 

def is_anagram( s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
### test cases below ####
s = "racecar"
t = "carrace"
print(is_anagram(s,t))
