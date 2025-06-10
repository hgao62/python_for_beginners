# chapter 11: Error Handling

# 11.1 Handling Exceptions basic syntax
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Code to run if error happens
    print("Error: Division by zero is not allowed.")
    print(f"Error: {e}")


# 11.2 try/except/else/finally
# The else block runs if no exceptions were raised in the try block
# The finally block runs no matter what, even if an exception was raised
# Example of try/except/else/finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    print("Success:", result)
finally:
    print("This will always run")


# 11.3 generic exception handling
try:
    numbers = [1, 2, 3]
    index = 5
    result = numbers[index]  # This will raise an IndexError

except Exception as e:
    print("Something went wrong:", e)
