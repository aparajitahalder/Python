# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:20:40 2019

@author: Aparajita
"""

#%%
#1. Program to unpack a tuple in several variables
t=(1,2,3,4,5,'a')
a,b,c,d,e,f=t
print(t)
print(a,b,c,d,e,f)


#%%
#2. Program to add an item in a tuple
t=(1,2,3,4,5)
t2=()
item=input("Enter element to be added : ")
t2=(item,)
t=t+t2
print(t)


#%%
#3. Program to convert a tuple to a string
t=('a','p','a','r','a','j','i','t','a')
str=''.join(t)
print(str)


#%%
#4. Program to create the colon of a tuple
from copy import deepcopy
t = ('a',1,2,[],7) 
print(t)
t2= deepcopy(t)
t2[3].append("Hola!")
print(t2)


#%%
#5. Program to convert a list to a tuple
l1=[1,2,3,'a',90]
t=tuple(l1)
print(l1)
print(t)


#%%
#6. Program to convert a tuple to a dictionary
t=(('a',1),('b',2),('c',3))
d=(dict((x,y) for x,y in t))
print(d)


#%%
#7. Program to replace last value of tuples in a list
t=((1,2,3),(4,5,6),(7,8,9))
t2=[i[:-1]+(0,) for i in t]
t2


#%%
#8. Program to remove an empty tuple(s) from a list of tuples
t=(1,2,3,(),4,5,(),6,7,(),8,9)
t2=[i for i in t if i]
t2


#%%
#9. Program to unzip a list of tuples into individual lists
t=((1,2,3),(4,5,6),(7,8,9))
l=[list(i) for i in t]
l


#%%
#10. program to count the elements in a list until an element is a tuple
l=[1,2,3,[4,5],(6,7),8,9]
t=[i for i in l if not isinstance(i,tuple)]
t










