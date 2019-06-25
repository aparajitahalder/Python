# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:37:25 2019

@author: Aparajita
"""

#%%
#1. Program to count the number of strings where the string length is 2 or more 
#   and the first and last character are same from a given list of strings
l=[]
a=input("ENTER THE STRINGS..... : ")
count=0
l=a.split()
for i in l:
    if len(i)>2 and i[0]==i[-1]:
            count=count+1
print(count)


#%%
#2. Program to sum and multiplies all the items in a list
i=5
list1=[]
for j in range(i):   
    l=int(input("ENTER THE ITEMS... : "))
    list1.append(l)
sum=0;mul=1
for i in list1:
    sum=sum+i
    mul=mul*i
print(sum,mul) 


#%%
#3. Program to find the list of words that are longer than n from a given list of words   
n=int(input("ENTER THE n VALUE : "))
l=input("Enter the list elements : ").split()
for i in l:
    if len(i)>n:
        print(i,end=" ")
        
        
#%%
#4. Program to generate and print a list of first and last 5 elements 
#   where the values are square of numbers between 1 and 30  
l=[]
n=1
while(n>=1 and n<=30):
    l.append(n*n)
    n=n+1
print(l[0:5]+l[-6:-1])


#%%
#5. Program to check whether two lists are circularly identical
l1=[1,2,3,4,5]
l2=[2,3,4,5,1]
l3=[]
if len(l1)==len(l2):
    j=i=count=0
    while l1[i]!=l2[j] and count<len(l2)-1:
        j+=1
        count+=1
    for k in range(len(l2)):
        l3.append(l2[j])
        j+=1
        if j==len(l1):
            j=0 
    count=0
    for i in range(len(l3)):
        if l1[i]==l3[i]:
           count+=1
    if count==len(l1):
       print("LIST CIRCULARLY IDENTICAL...")
    else:
       print("LIST NOT CIRCULARLY IDENTICAL...")
else:
    print("List not circularly identical...")        
           

#%%
#6. Program to get unique values from a list           
l=[]
l2=[]
d=dict()
for i in range(7):
    a=input("ENTER LIST ELEMENTS...")
    l.append(a)
for i in l:
    if i in d:
       d[i]+=1
    else:
       d[i]=1
for i in d:
    if d[i]==1:
        l2.append(i)
print(l2)


#%%
#7. Program to create a list by concatenating a given list which range goes from 1 to n 
n=int(input("Enter value of N : "))
l=['p','q','r']
l1=[]
for i in range(n):
    for j in l:
        l1.append(j)
print(l1)              


#%%
#8. Program to generate groups of five consecutive numbers in a list                 
b=[]
f=[]
for i in range(5):
    b=[]
    for j in range(1,6):
        c=5*i+j
        b.append(c)
    f.append(b)
print(f)
   
      
#%%
#9. Split a list every Nth element  
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
l2=[]
n=int(input("Enter the nth element : "))
for i in range(n):
    l2.append(list(l[i::n]))
l2


#%%
#10. Program to compute the similarity between two lists
l1=["red", "orange", "green", "blue", "white"]
l2=["black", "yellow", "green", "blue"]
l3=[]
l4=[]
for i in range(len(l1)):
    if l1[i] not in l2:
        l3.append((l1[i]))
print(l3)
for i in range(len(l2)):
    if l2[i] not in l1:
        l4.append((l2[i]))
print(l4)
  



