#!/usr/bin/env python
# coding: utf-8

# # 1- What are keywords in python?Using the keyword library , print all the python keywords.
keywords are reserved words in python that has specific use in program.
We cannot use keywords as variable to store values.


#print of all keywords using keyword ibrary
import keyword
print(keyword.kwlist)

output:
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    
# # 2-What are the rules to create variables in python?
rules to create variables in python:
    ->it should start with alphabet
    ->it should not start with numbers
    ->it may contain numbers but not at the starting og declaration.
    ->special chharacter cannot be used except underscore
    ->we can also use underscore at starting of variable declaration
    
# # 3-What are the standars and conventions followed for the nomenclature of variables in python to improve code readability and maintainability?
Variables names should be lowercase,with words separated by underscores as necessary to improve readability.

# # 4-What will happen if a keyword is used as a variable name?
Let's try to declare keyword as variable:-
True=45
output:
    True=45
    ^
SyntaxError: cannot assign to True
    
We will get error if we do so,hence keyword cannot be used as variable
# # 5-For what purpose def keyword is used?
def keyword is used to define a function.It is placed before a function name that is provided by the used to create a user-defined function.
# # 6-What is the operation of this special character  ' \ '?
In python , the backslash(\) is use in front of another character , it changes the meaning of that character.
example:\t act as a tab character
\n use as new line character.
# # 7-Give an xample of the following conditions:
i) Homogeneous list:
    l1=[1,2,3,4,5,6]
    l2=['hello','welcome','to','the','world','of','programming']
ii) Heterogeneous set:
     s={23,60,'apple','tom',80.9,'d'}
iii) Homogeneous tuple:
    t=(5,7,8,10,15)
# # 8-Explain the mutable data types with proper explanation & examples.
List of mutuable data types:
    ->list
    ->dictionaries
    ->sets
    ->user-defined classes
List=
my_list = [1, 2, 3]
print("my_list:", my_list)
output:
    my_list: [1, 2, 3] 
my_list.append(4)
print("my_list:", my_list)
output:
    my_list: [1, 2, 3, 4] 
        
dictionaries=
d={'name':'tom','phone_no':3435465,'gmail':'tom123@gmail.com'}
print(d)
d['adress']='crrcfvbtb'
print(d)
output:
    {'name': 'tom', 'phone_no': 3435465, 'gmail': 'tom123@gmail.com'}
{'name': 'tom', 'phone_no': 3435465, 'gmail': 'tom123@gmail.com', 'adress': 'crrcfvbtb'}

set=
s={3,4,6,'hello'}
print(s)
s.add('world')
print(s)

output:
    {'hello', 3, 4, 6}
    {'hello', 3, 'world', 4, 6}
    

# # 9-Write a code to create the given structure using only for loop: 
#         *
#        ***
#       *****
#      *******
#     *********

# In[91]:


n=5
space=n
for i in range(1,10,2):
    for j in range(space):
        print(' ',end=' ')
    space=space-1
        
    for k in range(i):
        print('*',end=' ')
        
    print('\n')
    
  


# # 10-Write a code to create the give structure using while loop:
#       ||||||||| 
#        |||||||
#         |||||
#          |||
#           |

# In[2]:


rows = 5
spaces = 0
stars = 9

while rows > 0:
    # Print spaces
    for i in range(spaces):
        print(" ", end="")

    # Print stars
    for j in range(stars):
        print("|", end="")

    # Move to the next line
    print()

    spaces += 1
    stars -= 2
    rows -= 1
   
   

    


# In[ ]:




