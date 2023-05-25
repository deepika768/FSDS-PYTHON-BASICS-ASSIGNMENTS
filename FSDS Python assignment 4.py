#!/usr/bin/env python
# coding: utf-8

# # 1-What exactly is []? 
[]-Represents a blank list.
# # 2-In a list of values stored in a variable called spam,how would you assign the vaue 'hello' as the third value?(Assume[2,4,6,10]are in spam)
let spam =[2,4,6,10] ,then we can write the below code:
spam=[2,4,6,10]
spam[2]='hello'
print(spam)
outut:
    [2, 4, 'hello', 10]
# # Let's pretend the spam includes the list['a','b','c','d'] for the next three queries

# # 3-What is the value of spam[int(int('3'*2)/11)]?
following steps shows how the above expression can be solved:
->'3'*2 gives 33 as a string
->int('33') gives 33
->33/11 gives 3.0
->int(3.0) gives 3
->now spam[3] gives 'd'
# In[3]:


spam=['a','b','c','d']
print(spam[int(int('3'*2)/11)])


# # 4-What is the value of spam[-1]?
spam[-1] gives 'd'
# # 5-What is the value of spam[:2]?
spam[:2] gives ['a','b']
# # Let's pretend bacon has the list[3.14,'cat',11,'cat',True] for the next three questions.

# # 6-What is the value of bacon.index('cat')?
bacon.index('cat') gives index of cat that is 1.
# In[10]:


bacon=[3.14,'cat',11,'cat',True]
bacon.remove('cat')
print(bacon)


# # 7-How does bacon.append(99) change the look of the list value in bacon?
 If we perform bacon.append(99) then 99 will be added to list in last that is in 5 th index and 6 th position.
 bacon=[3,14,'cat',11,'cat',True,99]   
# # 8-How does bacon.remove('cat') change the look of the list in bacon?
After performing the operation bacon.remove('cat') cat present at 1 index will be removed.
bacon will look like:
    [3.14, 11, 'cat', True]
# # 9-What are the list concatenation and list replication operators?
List concatenation is adding list by performing some operations.
example:
    l1=[1,2,3,4]
    l2=['apple','mango','banana']
    then simply writing l1+l2 will add both the 
    ists and will give [1,2,3,4,'apple','mango','banana'].
 we can also do concatenation by append function or extend or any other method.
 
 List replication:
 let l=[3,6,9,12,15]
 if we want to replicate this list 3 times then just write 
 l*3 
 which will give 
 [3,6,9,12,15,3,6,9,12,15,3,6,9,12,15]
# # 10-What is difference between the list methods append() andinsert()
append() method add the given value to the list in last index where as insert() method add the value at index given by user by pusing forward the value in that particular index.


l1=[1,2,3,4]
l1.append(9)
print(l1)
l1.insert(3,6)
print(l1)

output:
    [1, 2, 3, 4, 9]
    [1, 2, 3, 6, 4, 9]
# # 11-What are the two methods for removing items from a list?
Two methods for removing items from a list are remove() method and pop()
remove()- it will remove the value given by the user from the list
pop()-it will remove the value from the index given by the users from the list

l1=[1,2,3,4]
l1.remove(3)
print(l1)
output:
    [1, 2, 4]
l1=[1,2,3,4]
l1.pop(1)
print(l1)
output:
    [1, 3, 4]
    
# # 12-Describe how list values and string values are identical.
List and string both are used to store value /data and both are sequence.
# # 13-What'sthe difference between tuples and lists?
Tuples-stores data enclosed in () and are immutable that is we cannot alter the value.
List-stores data enclosed in [] and are mutable that is we can change the value or add values.
# # 14-How do you type a tuple value that only contains the integer 42?
t = (42,)
type(t)
output:
    tuple
# # 15-How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?
Suppose t=(1,2,3,4)
now if we want to convert it to list than we can write list(t),it will change to list.
print(t)
print(list(t))
output:
    (1, 2, 3, 4)
    [1, 2, 3, 4]
Now suppose l=[4,6,8,10]
we can convert the above list to tuple by writhing tuple(l), it will change list to tuple.
print(l)
print(tuple(l))
output:
    [4, 6, 8, 10]
    (4, 6, 8, 10)

    
# # 16-Variables that "contain" list values are not necesarily list themselves.Instead, what do they contain?
Element of list
# # 17-How do you distinguish between copy.copy() and copy.deecopy()?
In the case of copy(), a reference of an object is copied into another object. It means that any changes made to a copy of an object do reflect in the original object. In python, this is implemented using the “copy()” function. 
example:
    import copy
    l=[9,6,10]
    print(l)
    l=copy.copy(l)
    l.insert(1,12)
    print(l)
    output:
       
     [9, 6, 10]
     [9, 12, 6, 10]

 In the case of deepcopy(), a copy of the object is copied into another object. It means that any changes made to a copy of the object do not reflect in the original object. 
 
 example:
 import copy
 
# initializing list 1
li1 = [1, 2, [3,5], 4]
 
# using deepcopy to deep copy
li2 = copy.deepcopy(li1)
 
# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 
print("\r")
 
# adding and element to new list
li2[2][0] = 7
 
# Change is reflected in l2
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
 
print("\r")
 
# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")
 output:
    The original elements before deep copying
    1 2 [3, 5] 4 
    The new list of elements after deep copying 
    1 2 [7, 5] 4 
    The original elements after deep copying
    1 2 [3, 5] 4 
# In[ ]:




