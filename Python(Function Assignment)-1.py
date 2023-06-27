#!/usr/bin/env python
# coding: utf-8

# # 1-In python,what is the difference between a built-in function and a user-defined function?Provide an example of each. 
Built-in function are part of python language.They are provided to be used in our python program.
Example:-
    print() function
    
    
User-defined function are defined by user and can be execute by calling the function.
Example:-
    def add():
        a=9
        b=8
        print("sum is",a+b)
    add()
    
output:sum is 17
# # 2-How can you pass arguments to a function in python?Explain the difference between positional arguments and keyword arguments.
While calling we can give value ;
for example:
def sum(a,b):
    return a+b
print(sum(10,12))


positional arguments:-we must pass these arguments in the order defined by the function.
 example:
        def subtraction(a,b):
            return a-b
        print(subtraction(10,5))
        
Keyword arguments:- we pass arguments to the function through keyword argument with default value.
 example:
        def subtraction(a=0,b=0):
            return a-b
        print(subtraction(a=10,b=20))
        print(subtraction(b=10,a=5))
# In[4]:


def subtraction(a=0,b=0):
    return a-b
print(subtraction(a=10,b=20))
print(subtraction(b=5,a=15))


# # 3-What is the purpose of the return statement in a function?Can a function have multiple return statements? Explain with an example.
Purpose of return statement in a function is to return the value of its expression to the caller.
A function can have multiple returns, the one that satisfies the condition will be executed first and the function will exit.

Example:
    def type_of_int(i):
    if i % 2 == 0:
        return 'even'
    else:
        return 'odd'
 
    result = type_of_int(7)
 
    print(result)
    
    
output=odd
# # 4-What are a lambda functions in python? How are they different from regular functions? Provide an example where a lambda function can be useful.
Lambda function is a anonymous function which means function without name.

In regular function we need to give a name but in case of lamda function we don't need to define a name.
It is one line function with multiple arguments.They can be used whenever funtion arguments is necessary.

example:-
Lambda with Python’s Filter() function. This takes 2 arguments; one is a lambda function with a condition expression, two an iterable which for us is a series object. It returns a list of values that satisfy the condition.
list(filter(lambda x: x>18, df['age']))
# # 5-How does the concept of "scope" apply to functions in python? Explain the difference between local scope and global scope.
In Python, scope refers to the region of a program where a particular variable is accessible. When we define a function, the code inside it is indented and its scope changes to a new internal scope.


In Python, variables can have either a local scope or global scope123. Variables that are defined inside a function have local scope and can only be accessed within that specific function. Variables defined outside of any function or at the module level have global scope and can be accessed from anywhere within the module.
# # 6-How can you use the "return" statement in a Python function to return multiple values?
A tuple with multiple values separated by commas in the return statement. The caller can use unpacking syntax or starred expressions to access the values.
A list that contains multiple values in the return statement. The caller can use indexing or looping to access the values.
A dictionary that contains multiple records in the return statement. The caller can use keys or values to access the records.
# # 7-What is the difference between the "pass by value" and "pass by reference" concepts when it comes to function arguments in Python?
Pass by reference means that you have to pass the function(reference) to a variable which refers that the variable already exists in memory.

student = {'Jim': 12, 'Anna': 14, 'Preet': 10}
def test(student):
    new = {'Sam':20, 'Steve':21}
    student.update(new)
    print("Inside the function", student)
    return 
test(student)
print("Outside the function:", student)



In this approach, we pass a copy of actual variables in function as a parameter. Hence any modification on parameters inside the function will not reflect in the actual variable.

student = {'Jim': 12, 'Anna': 14, 'Preet': 10}
def test(student):
    student = {'Sam':20, 'Steve':21}
    print("Inside the function", student)
    return 
test(student)
print("Outside the function:", student)
# # 8-Create a function that can intake integer or decimal value and do following operations:

# # a)Logarithmic function(log x) b)exponential function(exp(x)) c)power function with base 2(2^x) d)square root
# 
# 

# In[43]:


import decimal
import math

def operations():
    value=float(input("enter a integer or decimal:"))
    a= decimal.Decimal(value).ln()
    b= "{:e}".format(value)
    c=pow(2,value)
    d= math.sqrt(value)
    return a,b,c,d

print(operations())


# # 9-Create a function that takes a full name as an argument and returns first name and last name.

# In[33]:


def first_name(name):
    n=name.split()
    return n[0]
name =input("enter full name")
print("first_name : ",first_name(name))

