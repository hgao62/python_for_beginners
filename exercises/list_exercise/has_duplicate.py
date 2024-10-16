from typing import List
'''
Duplicate Integer
Given an integer array nums, please complete has_duplicate function below so that it return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

'''


def has_duplicate(nums: List[int]) -> bool:
    pass# remove this line and add your code here






### test cases below ####
assert has_duplicate([1, 2, 3, 3])==True, "expect True"
assert has_duplicate([1, 2, 3, 4])==False, "expect False"
assert has_duplicate([])==False, "expect False"