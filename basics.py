#1. data types
age = 25 # integer
temperature = 98.6 # float
is_true = True # boolean
name = "alice" # string
customer_names = ["gorge", "trump", "james"] # list
people_age_map = {"gorge":24, "trump":80, "james":30} # dictionary
coordinates = (180,90) # tuple

#1.1 access element in list. use index(start from 0)
customer_names[0] # output gorge
customer_names[2] # output james
customer_names[-1] # access last item from list output james
#1.2 access element in dictionary. use key
people_age_map["james"]

#2. naming convention(snake case in python)
healthy_food_2 = "veg" # good
healthyFood = "veg" # bad because its not snake case
HealthyFood = "veg" # bad because its not snake case
i = "james" # bad because it's not descriptive
name = "james" # good


#3. if else
price = 100
if price < 100:
    print("cheap")
else:
    print("expensive")

#4. for loop: iterate through list
customer_names = ["gorge", "trump", "james"] # list
for name in customer_names:
    print(name)
#4.1 for loop: iterate through dictionary
car_price_map = {"honda":20000, "audi":60000, "porsche":100000, "ferrai":2500000}
for car_model, car_price in car_price_map.items(): # unpack dictionary key, value
    if car_price <= 30000:
        category = "economic"
    elif car_price < 150000:
        category = "luxury"
    elif car_price > 200000:
        category = "super car"
        

# 5 math operation
price = 10
price = price +5 # addition
price = price/5 # division
price = price - 5 # subtraction
price = price * 5 # products
remainder = 10 % 3 # module


#6 assignment use single equal sign
num1 =1
num2 =2
product = num1*num2
#6 comparison, use double if equal sign
even_numbers = []
if num1 %2 == 0:
    even_numbers.append(num1)

#Exercise 1 (考查 for loop, if else, math operation)
#find the even numbers for numbers variable below 
# and store all the even numbers in a variable called even_numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [] # initialize empty list
for number in numbers: # note 2. use appropriate variable name
    if number % 2 == 0:# note 1.double equal sign for comparison
        print(number)  # note 3. understand ident 
        even_numbers.append(number) # note 4. use append to add element to list
        
print(even_numbers)