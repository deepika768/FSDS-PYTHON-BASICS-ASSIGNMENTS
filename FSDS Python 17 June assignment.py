#!/usr/bin/env python
# coding: utf-8

# # 1. What is the role of try and exception block?

# Try and except block use to handle error,
# try block tests the code of erroe and except 
# block handle the error.
# 
# Try and except block plays a major role while writimg lengthy programs
# as some errors can be handle very easily without giving error in output and program run smoothly

# # 2. What is the syntax for a basic try-except block?

# try:
#     conditions or expression
# except Exceptions:
#     handle the error
#     

# # 3-What happens if an exception occurs inside a try block and there is no matchingexcept block?

# If an exceptions occurs inside the try block ,nothing after the exception block get executed,the execution will jump to catch block and then  finally block

# # 4. What is the difference between using a bare except block and specifying a specificexception type?

# Bare except block end up catching any and all kind of exception where as specific exception accept only exceptions itself or anything that inherits from it.

# # 5-Can you have nested try-except blocks in Python? If yes, then give an example.

# Yes we can have nested try-except blocks in python
# try:
#    print("outer try block")
#    try:
#        print("Inner try block")
#    except ZeroDivisionError:
#        print("Inner except block")
#    finally:
#        print("Inner finally block")
# except:
#    print("outer except block")
# finally:
#    print("outer finally block")

# # 6.Can we use multiple exception blocks, if yes then give an example.

# Yes, you can use multiple exception blocks in Python. For each try block, there can be zero or more except blocks. Multiple except blocks allow us to handle each exception differently. The argument type of each except block indicates the type of exception that can be handled by it. For example, you can catch different exceptions and do different things with them. You can also throw multiple different exceptions, but this can never happen at the same time.

# # 7.Write the reason due to which following errors are raised:

# a-EOF Error -The reason that EOFError occurs is that Python attempts to print out your input in variable string when no data is given. Generally, this error shouldn't pop up when you press your Enter key as input as it registers the variable as a string in your code.
# 
# b-FloatingPointError-Floating point numbers are limited in size, so they can theoretically only represent certain numbers. Everything that is inbetween has to be rounded to the closest possible number. This can cause (often very small) errors in a number that is stored.
# 
# c-IndexError- this occur when the index doesn't lies in the range of index of the list.
# 
# d-MemoryError-this error can due to:
#                   Outdated software and drivers
#                   Corrupt files
#                   Hardware failure, especially with your RAM or harddrive
#                   Faulty RAM
#                   
# e-OverflowError-whe a large number is run and system unable to handle then this error occur.
# 
# f-TabError-A TabError occurs when you indent the code using a combination of whitespaces and tabs in the same code block.
# 
# g-ValueError-Most of the time, value errors occur, when you try to convert a string to a number, which isn't a number. 
# For example: >>> int ("13a")

# # 8-Write code for the following given scenario and add try-exception block to it.

# In[1]:


#a-program to divide two numbers
a=int(input("giva a number:"))
b=int(input("give a number:"))
try:
    d=a/b
except ZeroDivisionError:
    print("give a non zero input")


# In[3]:


#b-program to convert a string to an integer
s=input("enter a string:")
try:
    n=int(s)
except:
    print("give a integer value inside string")


# In[3]:


#c-program to access an element in a list
l=[1,2,5,8,9,12]
try:
    print(l[2])
except IndexError:
    print("index out of range")
    
    

try:
    print(l[6])
except IndexError:
    print("index out of range")


# In[6]:


#d-Program to handle  specific exception
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")


# In[5]:


#e-program to handle any exception
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")


# In[ ]:




