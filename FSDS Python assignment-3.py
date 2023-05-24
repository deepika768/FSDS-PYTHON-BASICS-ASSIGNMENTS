#!/usr/bin/env python
# coding: utf-8

# # 1-Why are functions advantageous to have in your program?
Advantages of using Functions in a program:
    ->reducing duplication of code
    ->improved reusability of code
    ->write clearer code
    ->bigger problems are broken down into smaller problems.
# # 2-When does the code in a function run:when it's specified or when it's called?
When it is called then only its runs
# # 3-What statement creates a function?
In python function is created by def keyword,followed by function name(which is user defined) and parenthesis with or without argument.
# # 4-What is the difference between a function and a function call?
 A function is procedure to achieve a particular result.A function is defined separately.
While a function call is used to the call the function to execute the result.
# # 5-How many global scopes are there in a python  program? How many local scopes?
There is only one global scope in python program.
There can be more than one local scope in python program.
# # 6.What happens to variable in a local scope when the function call returns?
When the function call returns the variable in local scope destroyed, their values are no longer accessible or stored in memory.
# # 7-What is the concept of a return value? Is it possible to have return value in an expression?
A return statement is used to end  the execution of a function call and return the result to the caller.
# # 8-If a function does not have a return statement,what is the return value of a call to that function?
If a function doesnot have a return statement it returns none.
# # 9-How do you make a function variable refer to the global variable?
we have to write global along with global variable name inside the function.
# # 10-What is the data type for none?
' None'key word is used to define a none value.
print(type(None))
outpur-<class 'NoneType'>

# # 11-What does the sentence import areallyourpetsnamederic do?
This sentence is invalid and does not import any module. 
# # 12-If you had a bacon() feature in a spam module ,what would you call it after importing spam?
 After importing spam module , we can call bacon() function by writing 'spam.bacon()'.
# # 13- What can you do to save a programme from crashing if it encounters an error?
We can use try and except to code so that we can save program from crashing.

try:
    code
except:
    print("error message")
    
# # 14-What is the purpose of the try clause? What is the purpose of the except clause?
Try- this block checks the excepted error to occur.
Except-this block handle the error
# In[ ]:




