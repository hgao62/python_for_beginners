"""To define a set in Python, you use the curly brace {}
A Python set is an unordered list of immutable elements. It means:

Elements in a set are unordered.
Elements in a set are unique. A set doesn’t allow duplicate elements.
Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.

"""

skills = {'Python programming','Databases', 'Software design'}
empty_set = set()

# An empty set evaluates to False in Boolean context. For example:
skills = set()

if not skills:
    print('Empty sets are falsy')
    
    
# To check if a set contains an element, you use the in operator:
# element in set
    
ratings = {1, 2, 3, 4, 5}
rating = 1

if rating in ratings:
    print(f'The set contains {rating}')
    
    
# add element to set
skills = {'Python programming', 'Software design'}
skills.add('Problem solving')

print(skills)

# remove an element from a set,

skills = {'Problem solving', 'Software design', 'Python programming'}
skills.remove('Software design')

print(skills)



import pandas as pd

trans_data = pd.read_csv("trans.csv")
mapping_data = pd.read_csv("mapping.csv")

enriched_trans_data = pd.merge(trans_data, mapping_data, on="distributor name", how="inner")
customer_mapping_data = pd.read_csv(r"c:\temP\customer.csv")
trans_data_with_cleaned_customer_name = pd.merge(enriched_trans_data,customer_mapping_data,on ="customer name")

def clean_internal_name(trans_data):
    mapping_data = pd.read_csv("mapping.csv")
    enriched_trans_data = pd.merge(trans_data, mapping_data, on="distributor name", how="inner")
    return enriched_trans_data


nov_trans_data = pd.read_csv()
nov_cleaned_trans_data = clean_internal_name(nov_trans_data)


def