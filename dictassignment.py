# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:12:57 2019

@author: Aparajita
"""
#%%
#1. Program to count the number of characters (character frequency) in a string
d={}
s=input("Enter the string")
count=1
for i in s:
    if i in d:
        d[i]=count+1
    else:
        d[i]=count
d


#%%
#2. Program to convert list to list of dictionaries
l1=["Black", "Red", "Maroon", "Yellow"]
l2=["#000000", "#FF0000", "#800000", "#FFFF00"]
l3=['color_name', 'color_code']
l4=[]
d={}
for i in range(4):
    d[l3[0]]=l1[i]
    d[l3[1]]=l2[i]
    l4.append(d)
l4


#%%
#3. Script to sort (ascending and descending) a dictionary by value
import operator 
d={1: 10, 2: 20, 3: 30, 4: 400, 5: 50, 6: 60}
t=sorted(d.items(),key=operator.itemgetter(1))


#%%
#4. Script to concatenate following dictionaries to create a new one
dict1={1:10, 2:20} 
dict2={3:30, 4:40} 
dict3={5:50,6:60}
d={}
for i in dict1:
    d[i]=dict1[i]
for i in dict2:
    d[i]=dict2[i]
for i in dict3:
    d[i]=dict3[i]
d   


#%%
#5. Script to check if a given key already exists in a dictionary 
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n=int(input("Enter the key to be checked : "))
if n in d:
    print("Key Exists...")
else:
    print("Key not Exists...")
    
    
#%%
#6. script to generate and print a dictionary that contains 
#   a number (between 1 and n) in the form (x, x*x)
n=int(input("Enter the no. : "))
d={}
for i in range(1,n+1):
    d[i]=i*i
d


#%%
#7. Program to sum all the items in a dictionary
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
a=d.items()
a
sum=0
for i in a:
    sum+=i[0]+i[1]
sum


#%%
#8. Program to combine two dictionary adding values for common keys
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
for i in d2:
    if i not in d3:
        d3[i]=d2[i]
d3


#%%
#9. Program to create and display all combinations of letters, 
#   selecting each letter from a different key in a dictionary
d={1:['a','b'],2:['c','d']}
l1=d.get(1)
l2=d.get(2)
for i in range(2):
    for j in range(2):
        print(l1[i]+l2[j])


#%%
#10. Python program to create a dictionary from a string.
str1=input("Enter the String : ")
d={}
count=0
for i in str1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
d


#%%























