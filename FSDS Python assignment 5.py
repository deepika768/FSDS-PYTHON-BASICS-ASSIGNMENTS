#!/usr/bin/env python
# coding: utf-8

# # 1-What does an empty dictionary's code look like?
#empty dictionary code:
d={}
# # 2-What is the value of a dictionary value with the key 'foo' and the value 42?
{'foo':42}
# # 3-What is the most significant distinction between a dictionary and a list?
A list and a dictionary are different data structures in python.
A list is a collection of index value pairs, like an array, that can store any data types and is ordered and sequential. 
A list can be created by using brackets and commas.
 A list is fast for accessing elements by index.

A dictionary is a collection of key value pairs, like a hash table, that can store any data types and is not ordered and requires the keys to be hashable. A dictionary can be created by using braces and colons.A dictionary is fast for accessing elements by key
# # 4-What happens if you try to access spam['foo'] if spam is {'bar':100}?
spam={'bar':100}
spam['foo']
If we will perform this code this will obviously give us key erroras in dictionary there is no key named'foo'.
# # 5-If a dictionary is stored in a spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
In above 2 expression there is no difference as both checks whether 'cat' is present as key in dictionary.
# # 6-If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
'cat' in spam checks whether 'cat' is present as key in spam.
wheras 'cat' in spam.values() checks whether 'cat' is present as values in spam.
# # 7-What is a shortcut for the following code?if 'color' not in spam:spam['color']='black'
# 
spam.setdefault('color','black')
# # 8-How do you "pretty print" dictionary values using which module and function?
The module is pprint.
The functions are pprint.pprint() and pprint.pformat().
# In[ ]:




