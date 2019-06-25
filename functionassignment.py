# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:42:39 2019
s
@author: Aparajita
"""


#%%
#1. Function to create the HTML string with tags around the word(s)
# add_tags('i', 'Python') -> '<i>Python</i>'
def html(str1,an):
    print("<",an,">",str1,"</",an,">")
n=input("Enter the String : ")
a=input("Enter the Tag : ")
html(n,a)


#%%
#2. Function to insert a string in the middle of a string.
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
def InsertMiddle(an,str1):
    for i in range(len(an)):
        if(i==len(an)/2):
            print(str1,end="")
            print(an[i],end="")
        else:
            print(an[i],end="")
        
n=input("Enter the TAGS : ")
a=input("Enter the STRING : ")
InsertMiddle(n,a)


#%%
#3. Function to reverses a string if it's length is a multiple of 4
def reverse(str1):
    if(len(str1)%4==0):
        print(str1[::-1])
    else:
        print(str1)
n=input("Enter the no : ")
reverse(n)


#%%
#4. Check ifstring is pallindrome or not
def reverse(str1):
    #str2=reversed(str1)
    str2=str1[::-1]
    if str2==str1:
        print("String palllindrome")
    else:
        print("String not pallindrome")
n=input("Enter the String : ")
reverse(n)


#%%
#5. Function that prints out the first n rows of Pascal's triangle
def pascal(n):
   k=2*n
   for i in range(n):
        for s in range(k):
            print(" ",end="")
        for j in range(i+1):
            if j==0 or i==0:
                c=1
            else:
                c=int(c*(i-j+1)/j)
            print(c,end=" ")
        k-=1
        print("")
a=int(input("Enter the rows of Pascal table : "))
pascal(a)

    
#%%   
#6. Function that prints out the first n rows of Pascal's triangle
def isPangram(str1):
    str2="abcdefghijklmnopqrstuvwxyz"
    count=0
    for i in str2:
        if i in str1:
            count+=1
    if count>=26:
        print("String is Pangram...")
    else:
        print("String is not Pangram...")

n=input("Enter the String : ")
isPangram(n)


#%%
#7. Program that accepts a hyphen-separated sequence of words as input
#   Prints the words in a hyphen-separated sequence after sorting them alphabetically
def HypSepStr(str1):    
    str2=str1.split("-")
    print("-".join(sorted(str2)))
    
str1=input("Enter Hypen Seperated String : ")
HypSepStr(str1)


#%%
#8. Function to create and print a list where the values are square of numbers between 1 and 30
def square():
    l=[]
    for i in range(1,31):
        l.append(i*i)
    print(l)
square()


#%%
#9. Program to access a function inside a function
def funcInsideFunc():
    for i in range(1,11):
        print(outFunc(i))
        
def outFunc(j):
        return(j*j*j)
    
funcInsideFunc()   


#%%
#10. Function to check whether a number is perfect or not
def isPerfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if sum==n and (sum+n)/2==n:
        print("Function is Perfect")
    else:
        print("Function is not Perfect")
        
a=int(input("Enter the no. : "))    
isPerfect(a)   
    
    