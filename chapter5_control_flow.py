# Chapter 5: Control Flow

# 5.1 if elif else
# The if statement is used to test a condition.
# If the condition is true, the code block inside the if statement is executed.
# If the condition is false, the code block inside the else statement is executed.
# The elif statement is used to test multiple conditions.
# If the first condition is false, the code block inside the elif statement is executed.
# If the second condition is false, the code block inside the else statement is executed.
# else statement is executed if all the conditions are false.
# Example:
age = 25
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 5.2 for loop
# The for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# It is used to execute a block of code for each item in the sequence.
# Example:
customer_names = ["gorge", "trump", "james"]  # list
for name in customer_names:
    print(name)

# 5.3 range function
# The range function is used to generate a sequence of numbers.
# It is often used in for loops to specify the number of iterations.
# The range function can take one, two, or three arguments:
# 1. range(stop) - generates numbers from 0 to stop-1
# 2. range(start, stop) - generates numbers from start to stop-1
# 3. range(start, stop, step) - generates numbers from start to stop-1 with a step value

range(5)  # generates numbers from 0 to 4
range(1, 6)  # generates numbers from 1 to 5
range(1, 10, 2)  # generates numbers from 1 to 9 with a step of 2

for i in range(5):  # generates numbers from 0 to 4
    print(i)  # output: 0, 1, 2, 3, 4

for i in range(1, 6):  # generates numbers from 1 to 5
    print(i)  # output: 1, 2, 3, 4, 5

for i in range(1, 10, 2):  # generates numbers from 1 to 9 with a step of 2
    print(i)  # output: 1, 3, 5, 7, 9

# 5.4 while loop
# The while loop is used to execute a block of code as long as a condition is true.
# It is used to repeat a block of code until a condition is false.
# Example:
count = 0
while count < 5:
    print("Count is: ", count)
    count += 1  # increment count by 1


# 5.5 break statement
# The break statement is used to exit a loop prematurely.
# It is used to break out of the loop when a certain condition is met.
# Example:
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print(i)  # output: 0, 1, 2, 3, 4

# 5.6 continue statement
# The continue statement is used to skip the current iteration of a loop.
# It is used to skip the rest of the code inside the loop for the current iteration.
# Example:
for i in range(10):
    if i == 5:
        continue  # skip the rest of the code inside the loop when i is 5
    print(i)  # output: 0, 1, 2, 3, 4, 6, 7, 8, 9

# 5.7 pass statement
# The pass statement is used as a placeholder for future code.
# It is used when a statement is required syntactically but no code is needed.
# Example:
for i in range(10):
    if i == 5:
        pass  # do nothing when i is 5
    print(i)  # output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


# Exercise
# 5.1: Print even numbers from 1 to 20
for num in range(1, 21):
    if num % 2 == 0:
        print(num)  # Output: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

# 5.2  Print numbers from 1 to 10, but skip the number 5
for num in range(1, 11):
    if num == 5:
        continue  # Skip the number 5
    print(num)  # Output: 1, 2, 3, 4, 6, 7, 8, 9, 10

# 5.3 Print numbers from 1 to 10, but stop the loop when the number is 7
for num in range(1, 11):
    if num == 7:
        break  # Stop the loop when the number is 7
    print(num)  # Output: 1, 2, 3, 4, 5, 6

# 5.4 keep printing numbers as long as the number is less than 10
num = 0
while num < 10:
    print(num)  # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    num += 1  # Increment num by 1 each iteration
