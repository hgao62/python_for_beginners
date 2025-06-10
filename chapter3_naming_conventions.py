# Chapter 3 Naming Conventions

#Example:
#3.11
#bad
a = 5 # bad because its not descriptive
# good
price = 5 

#3.12
# bad because not snake case
customerNames = ["gorge", "trump", "james"] # bad because its not snake case
# good
customer_names = ["gorge", "trump", "james"] # good

#3.13
#bad  because it starts with a number
1name = "james" 
#good because it starts with a letter
name1 = "james" 

#3.14 bad because it starts with a special character
@name = "james" # bad because it starts with a special character
#good because it starts with a letter
name = "james" # good because it starts with a letter

#3.15 bad because it's too long
this_is_a_very_long_variable_name = "james" # bad because it's too long
#good because it's short
name = "james" # good because it's short

#3.16 bad because it uses reserved keywords
def = "james" # bad because it uses reserved keywords

#good because it doesn't use reserved keywords
name = "james" # good because it doesn't use reserved keywords