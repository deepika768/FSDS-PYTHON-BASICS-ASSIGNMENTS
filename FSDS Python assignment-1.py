#!/usr/bin/env python
# coding: utf-8

# # 1.In the below elements which of them are values or an expression? 
*      -> arithmetic operator(multiplicative operator)
'hello'-> string
-87.8  -> integer
-      -> arithmetic operator(subtraction)
/      -> arithmetic operator(division)
+      -> arithmetic operator(addition) 
6      -> integer
# # 2.What is the difference between string and variables?
String -> collection of characters or even a one character is called               strings. 
        It  is enclosed within single qoutation mark or double qoutation         mark.
        example:- 'd','apple',"weloce to the world."
Variables -> variables are basically storage box,where we store values                which is integer,float,double ,string,
             character or of any data type.
             example:- a=10,b='hey!!',l=[1,2,4]
# # 3.Describe three data types
list-collection of elements enclosed within square bracket which are          ordered,changeable and allow duplicate values.
     First element of list has index 0.Lists are mutable(we can change        or alter any values).
     examples-l=[1,2,3,4,5]
              l1=['apple','orange','papaya']
              l2=[45,60,80,'apple','pineapple',56.90]
            
Tuples-collection of elements enclosed within parenthesis which are              orderd and allow duplicates.
       First element of tuple has index 0.Tuples are immutable(we cannot        change or alter any values).
       example:- t=(1,2,4,5)
                 t=('hii','hello','hey')
                 t=('hello',1,'abc',56,90.9)
                    
Dictionaries-collection of data in form of key:value pair enclosed within              curly braces.
             Dictionaries are ordered, changeable,and doesnot allow                    duplicates.
            examples:- d=                                      {'name':'abc','gmail'='abc@gmail.com','number':1234}
                       d1={'fruit':'mango','vegetable':'cabbage'}
# # 4.what is an expression made up of? What do all expressions do?
An expression is made up of operands and operators.
Expressions do operations according to what operator is and also data types,
like if operator is addition or subtraction then operands should be of 
that is (integer and float) or (integer and integer) or (float or float)  or (string and string)
if the operator is multiplication it multiply (string and integer) or (integer or integer)
if the operator is division it will give float value as output
if the operator is // ,it will give quotient and if it is % ,it will give remainder.
There are more operators like relational operators which compare the operands and many more
# # 5.This assignment statements,like spam=10.What is the difference between an expression and a statement?
# 
An expession is a piece of code that is evaluated to a value.
example:- 23+67
          34>80
A statement is a piece of code that executes specific instruction or tells computer to complete the task.
example:- spam =10
          x=90

# # 6.After running the following code , what does the variable bacon contain?

# In[4]:


bacon=22
bacon+1


# # 7.What should the values of the following two terms be?

# In[5]:


'spam'+'spamspam'


# In[6]:


'spam'*3


# # 8.Why is eggs  valid variable name while 100 is invalid?
There is some rules to declare a variable.We cannot start a variable name with numbers or special characters (except underscore).
This is the reason why eggs is valis variable name whereas 100 is not a valid variable name. 
# # 9.What three functions can be used to get the integer,floating-point number,or string version of value?
To get an integer we use int() function.
example:- c=3/2
          print(int(c))
        output-1
To get a floating-point number we use float().
example:-
    a=9
    print(float(a))
output=9.0
To get a string version of a value we use str().
example:- b=94
          print(str(b))
        output-94
        but the type will be string
            

# # 10-Why does this expression cause an error?How can you fix it?
'I have eaten '+99+'burritos'
we cannot add string and integer ,hence we will get an error
fix-
'I have eaten '+'99'+'burritos'
now this statement will give result.
# In[19]:


'I have eaten '+'99'+'burritos'


# In[ ]:




