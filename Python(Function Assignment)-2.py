#!/usr/bin/env python
# coding: utf-8

# # 1-What is a lambda function in Python, and how does it differ from a regular function?
Lamda function is a anonymous function that doesn't have any name.They are defined with lambda keyword.
Lamda function are good for one line function.

Difference between lambda functions and regular functions is their syntax. Lambda functions are defined in a single line of code, whereas regular functions are defined with the def keyword and span multiple lines. 

Another difference is that lambda are more limited than regular functions, as they can only contain expression not statements.

# # 2-Can a lambda function in Python have multiple arguments? If yes, how can you define and usethem?

# In[27]:


Yes,Lambda function does have multiple arguments.
#program to return sum of 2 numbers using lambda function
x=int(input("enter first number:"))
y=int(input("enter second number:"))
sumation= lambda x,y: x+y 
print(sumation(x,y))


# # 3-How are lambda functions typically used in Python? Provide an example use case.
Use of lambda function in python:
->A squaring function
->A subtraction function with multiple arguments
->Using lambda with map() to make the map function more concise
->Using lambda with filter() to simplify the filter() function
->Using lambda with higher-order functions like reduce(), sort(), sorted(), min(), and max(

x=9
square=lambda x: x*x
square

# # 4-What are the advantages and limitations of lambda functions compared to regular functions inPython?
Advantages of lambda functions are:
->no need to think about name like we have to give in regular function.
->simple and easy to understand one line code
->no additonal variable are added.

Disadvantages of lambda functions are:
->Lambda expressions are a strange and unfamiliar syntax to many Python programmers.
->Lambda functions themselves lack names and documentation, meaning that the only way to know what they do is to read the code.
->Lambda expressions can only contain one statement, so some readable language features, such as tuple unpacking, cannot be used with them.
->Lambda functions can often be replaced with existing functions in the standard library or Python built-in functions.
# # 5-Are lambda functions in Python able to access variables defined outside of their own scope?Explain with an example.

# In[23]:


#Yes, lambda functions in Python can access variables defined outside of their own scope.
#example:
import functools

def buttonHandler(num):
    print('button', num)

def try_partial():
    handlers = []
    for num in range(5):
        handlers.append(functools.partial(buttonHandler, num))
    return handlers

print("test 3")
for handler in try_partial():
    handler()
   



# # 6-Write a lambda function to calculate the square of a given number.

# In[26]:


x=int(input("enter a number:"))
square=lambda x:x*x
print(square(x))


# # 7-Create a lambda function to find the maximum value in a list of integers.

# In[36]:


l1=[1,4,6,8,9,10,23,7]
maximum=lambda maximum:max(l1)
print(maximum(l1))


# # 8-Implement a lambda function to filter out all the even numbers from a list of integers.

# In[41]:


l1=[2,5,4,6,8,7,9,12,15,34,50,16]
print("old array is:",l1)

new_array=list(filter(lambda x:x%2==0,l1))
print("filtered list is:",new_array)


# # 9-Write a lambda function to sort a list of strings in ascending order based on the length of eachstring.

# In[47]:


l1=["apple","orange","grapes","mango","kiwi"]
l1.sort(key=lambda x:len(x))
print("sorted list:" , l1)


# # 10-Create a lambda function that takes two lists as input and returns a new list containing thecommon elements between the two lists.

# In[51]:


l1=[1,2,4,5,7,8,9]
l2=[3,4,8,9,10,4,5]
l3=lambda l1,l2:list(set(l1)&set(l2))
l3(l1,l2)


# # 11-Write a recursive function to calculate the factorial of a given positive integer.
def factorial(n):
    if (n==1 or n==0):
        return 1
     
    else:
        return (n * factorial(n - 1))
 
 #Driver Code
num = 6;
print("number : ",num)
print("Factorial : ",factorial(num))
# # 12-Implement a recursive function to compute the nth Fibonacci number.

# In[54]:


def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 

#Driver Program 
print(Fibonacci(10))


# # 13-Create a recursive function to find the sum of all the elements in a given list.

# In[57]:


def sum_list(arr,size):
    if size==0:
        return 0
    return arr[size-1]+sum_list(arr,size-1)
l=[1,4,6,7,8,9]
sum_list(l,len(l))


# # 14-Write a recursive function to determine whether a given string is a palindrome.

# In[66]:


def isPalRec(string,s,e):   
    # If there is only one character
    if (s == e):
        return True
 
    if (st[s] != st[e]) :
        return False
 
    if (s < e + 1) :
        return isPalRec(st, s + 1, e - 1);
 
    return True
 
def isPalindrome(st) :
    n = len(st)
     
    # An empty string is
    # considered as palindrome
    if (n == 0) :
        return True
     
    return isPalRec(st, 0, n - 1);
 
 
# Driver Code
st = "geeg"
if (isPalindrome(st)) :
    print ("Yes")
else :
    print ("No")


# # 15-Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.

# In[68]:


def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

gcd(9,12)

