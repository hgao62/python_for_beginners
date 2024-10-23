# Python uses the square brackets ([]) to indicate a list
empty_list = []

# 1 modify element in list
numbers = [1, 3, 2, 7, 9, 4]
numbers[0] = 10
numbers[1] = numbers[1]*10
# 2 add elements to the list
numbers = [1, 3, 2, 7, 9, 4]
numbers.append(100)
#2.1 add element to any position in the list
numbers.insert(2,100)#index, number

# 3 remove elements from list
numbers = [1, 3, 2, 7, 9, 4]
# 3.1 remove last elements
numbers.pop()
# 3.2 remove from certain index
numbers.pop(1) # remove second element

# 3.2 remove by value
numbers.remove(9) # delete 9 from list

# 4 index slicing
numbers = [1, 3, 2, 7, 9, 4]
numbers[0:3]# left inclusive, right not

# 4.1 get first n elements from list
numbers[:4]

# 5 sort a list
# 5.1 sort in place
numbers = [1, 3, 2, 7, 9, 4]
1 in numbers
numbers.sort()
numbers.sort(reverse=True)
# 5.2 sort to return a new list
sorted_numbers = sorted(numbers)

# 6 list  comprehension(超高频面试题)
makeup_prices = [100, 120, 130, 140, 150] # 30% off
discount_prices = []
for price in makeup_prices:
    discount_prices.append(price*0.7)
    
discount_prices = [price*0.7 for price in makeup_prices]

all_numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in all_numbers if number %2 ==0]
# Summary
# Use list[index] = new_value to modify an element from a list.
# Use append() to add a new element to the end of a list.
# Use insert() to add a new element at a position in a list.
# Use pop() to remove an element from a list and return that element.
# Use remove() to remove an element from a list.
# Use list[start_index: end_index] to slice index