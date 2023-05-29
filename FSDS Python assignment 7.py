#!/usr/bin/env python
# coding: utf-8

# # 1-Create two int type variables,apply addition,subtraction,division,and multiplications and store the results in variables.Then print the data in the following format by calling the variable:

# In[5]:


a=10
b=2
print("First variable is",a,'&',"second variable is",b)
add=a+b
print("Addition:",a,'+',b,'=',add)
sub=a-b
print("Subtraction:",a,'-',b,'=',sub)
mult=a*b
print("Multiplication:",a,'*',b,'=',mult)
div=a/b
print("Division:",a,'/',b,'=',div)


# # 2-What is the difference between the following operators:
#'/' & '//'
'/'-this operators gives output in float type.
    example:
        5/2 gives 2.5
'//'-this operator gives only qoutient
     example:
        5/2 gives 2
#'**' & '^'
'**'-this operator gives power raised to the particular input.
     example:
        5**2 gives 25

'^'-Each bit position in the result is the logical XOR of the bits in the corresponding position of the operands. (1 if the bits in the operands are different, 0 if they are the same.)
    example:
        4^4 gives 0
        4^2 gives 6
        
# # 3-List the logical operators.
logical operators are not, or and and
# # 4-Explain right shift operator and left shift operator with examples.
Right shift-Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two.
example:
    a = 10 = 0000 1010 (Binary)
    a >> 1 = 0000 0101 = 5

Left shift- Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.
exampe: 
    a = 5 = 0000 0101 (Binary)
    a << 1 = 0000 1010 = 10
    a << 2 = 0001 0100 = 20 
# # 5-Create a list containinng int type data of length 15.Then write a code to check if 10 is present in list or not.

# In[18]:


l=[4,5,8,9,10,12,17,20,26,29,30,35,39,34,40]
len(l)
for i in range(len(l)):
    if l[i]==10:
        print("number found in ",i)


# In[ ]:





# In[ ]:





# In[ ]:




