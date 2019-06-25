# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:06:55 2019

@author: Aparajita
"""

#%%
#1. Takes full name as input and print first and middle name as abbreviation
str1=input("ENTER YOUR FULL NAME : ")
a=list(str1.split())
str2=""
for i in range(len(a)-1):
    str2+=a[i][0]+'.'
str2=str2+' '+a[2]
print(str2)


#%%
#2. Take string from a given string and convert its first character into '$'
str1=input("ENTER THE STRINGS : ")
a=str1[0]
str1=str1.replace(a,'$')
str1=a+str1[1:]
print(str1)


#%%
#3. Swap first character of two strings and merge them into single string
str1=input("ENTER FIRST STRING : ")
str2=input("ENTER SECOND STRING : ")
a=str1[0]
b=str2[0]
str3=b+str1[1:]+" "+a+str2[1:]
print(str3)


#%%
#4. Print first and last two characters of a string
str1=input("ENTER THE STRING : ")
str3=str1[0:2]+str1[-2:]
if len(str1)>2:
     print(str3)
else:
    str3=" "
    print(str3)

    
#%%
#5. Function takes a list of words and returns the length of the longest one
def longword(list1=[]):
    a=len(list1[0])
    for i in range(1,5):
        if len(list1[i])>a:
            a=len(list1[i])
    return a

list1=[]
for i in range(5):
    c=input("ENTER STRINGS : ")
    list1.append(c)
list1
b=longword(list1)    
print(b)       
        
    
#%%
#6. Remove the characters which have odd index values of a given string    
str1=input("ENTER THE STRING : ")
str2=""  
for i in range(len(str1)):
    if i%2==0:
        str2=str2+str1[i]
str1=str2
print(str1)


#%%
#7. Count the occurrences of each word in a given sentence
str1=input("ENTER THE STRING : ")
count=dict()
words=str1.split()

for i in words :
    if i in count:
        count[i]+=1
    else:
        count[i]=1
        
print(count)


#%%
#8.  Prints the unique words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red
#6. Program to get unique values from a list           
l=[]
l2=[]
for i in range(7):
    a=input("ENTER LIST ELEMENTS...")
    l.append(a)
for i in range(len(l)):
    if l[i] not in l2:
        j=i+1
        while(j!=len(l)):
            if l[i]==l[j]:
                count=count+1
            j+=1
        if count==1:
            l2.append(l[i])
    count=1
print(sorted(l2))



#%%
#9. Add a prefix text to all of the lines in a string
#str1=input("ENTER THE STRING : ")
str3='''I am a CSE Student.
        I want to be a superb AI Engineer
        Someday, my dream will definitely come true...'''
a=list(str3.split('\n'))
str2=" "
for i in a:
    str2+="$"+i+"\n"    
print(str2)    
    
#%%
#10. Reverse a string
str1=input("ENTER THE STRING : ")
print(str1[::-1]) 


#%%
#11. Count repeated characters in 'thequickbrownfoxjumpsoverthelazydog'
str1="thequickbrownfoxjumpsoverthelazydog"
a=list(str1)
count=dict()
for i in a:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)


#%%
#12. Convert string into list
str1=input("ENTER THE STRING : ")
str2=list(str1.split())
str2    
    
   
#%% 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






