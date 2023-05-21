#!/usr/bin/env python
# coding: utf-8

# # 1-What are the two values of the boolean data type? How do you write them?
Two values of boolean data type is True and False.
To write true start with capital T and others to be small that is True
and to write false follow same as true
# # 2-What are the three different types of boolean operators?
Three different types of boolean operator are:
    ->and operator
        
    ->or operator
       
    ->not operator
        
# # 3-Make a list of each boolean operator's truth tables(i.e. every possible combination of boolean values for the operators and what it evaluate).
For and operator:
        True and True gives True
        False and False gives False
        True and False gives False
        False and False gives False
        
For or operator:
        True or True gives True
        False and False gives False
        True and False gives True 
        False and True gives True
        
For  not operator:
        not True gives False
        not True gives False
# # 4-What are the values of the following expressions?
(5>4) and (3==5)
   output-> False
not(5>4)
   output->False
(5>4) or (3==5)
   output->True
not((5>4) or (3==5))
   output->False
(True and True) and(True==False)
   output->False
(not False) or (not True)
   output->True
# # 5-What are the six comparison operator? 
Six comparison operator are:
    1-less than(<)
    2-greater than(>)
    3-less than equal to(<=)
    4-greater than equal to(>=)
    5-equal equal to(==)
    6-not equal to(!=)
# # 6-How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one:
Equal to (==) is  a relational  operator used to compare values and then return true or false.
example:
    a=10
    if a==10:
         return True
    
Assignment operators is assigning values to a variable.
example:
   a=5
   b='Tom'
   
   
#condition when we would use one:
when we have to compare values we use equal to , while writting if statementor while loops we use equal to .
when we want to assign value we use assignment operator
# # 7-Identify the three blocks in this code:
spam=0
if spam==10:      #if block to print eggs if spam is equal to 10
    print('eggs')
if spam>5:        #if block to print bacon if spam is greater than 5
    print('bacon')
else:           #if above conditions doesnot satisfies this block execute
    print('ham')
print('spam')
print('spam')
# # 8-Write a code that prints Hello if 1 is stored in spam,prints Howdy if 2 is spam,and prints Greetings! if anything else is stored in spam.
spam=0
if spam==1:
    print('Hello')
if spam==2:
    print('Howdy')
else:
    print('Greetings!')
    
# # 9-If your programme is stuck in an endless loop,what keys you'll press?
A programme can press ctrl+c ,if it doesnot work than restart window in case of jupyter notebook.
Otherwise have to close the window.
# # 10-How can you tell the difference between break and continue?
Break: break statement is used to terminate the loop or statement in which it is present.When the break statement is executed then the loop has to terminate,no more iteration can occur.
continue-continue statement is also a loop control statement just like break statement.
In case of continue statement instead of terminating the loop,it will force the loop to execute the next iteration.
When the continue statement is executed in the loop,the code inside the loop following the continue statement will skipped and the next iteration will begin.
# # 11-In a for loop,What is the difference between range(10),range(0,10),and range(0,10,1)?
If we run all three of these we will get the same output,just the writting ways are different.
In case of range(10)->it will print from 0 to 9
In case of range(0,10)->it will also print from 0 to 9
In case of range(0,10,1)->it will print from 0 to 9 with 1 gap in between.
# # 12-Write a short program that prints the numbers 1 to 10 using a for loop.then write an equivalent program that prints the number 1 to 10 using while loop.

# In[12]:


# using for loop
for i in range(10):
    print(i)
    
#using while loop
i=0
while i<10:
    print(i)
    i+=1


# # 13-If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# In[ ]:


We can call bacon() function by writing spam.bacon(). 

