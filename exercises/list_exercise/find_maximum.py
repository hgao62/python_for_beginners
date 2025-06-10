"""
Find Maximum: finds the maximum number in a list without using the built-in max() function.
"""
# 考察知识点
# 1. for loop
# 2. if statement
# 3. 怎么遍历 list
# 3 comparison operators

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

max_num = nums[0]  # Assume the first number is the maximum
for num in nums:
    if num > max_num:  # Compare each number with the current maximum
        max_num = num  # Update the maximum if a larger number is found

print("The maximum number in the list is:", max_num)  # Output the maximum number
