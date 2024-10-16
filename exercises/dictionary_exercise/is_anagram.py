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
    pass # remove this line and add your code here



### test cases below ####
s = "racecar", t = "carrace"
assert is_anagram(s,t), True
s = "jar", t = "jam"
assert is_anagram(s,t), False
assert is_anagram(s,t), False