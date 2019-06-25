# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:54:14 2019

@author: Aparajita
"""

#%%
#1. Program to read an entire text file
fo=open("data3.txt","a+")
fo.write("Python is a interpretor Language.")
str1=fo.read(25)
print(str1)
fo.close()


#%%
#2. Append text to a file and display the text
fo=open("data1.txt","a+")
str1=input("Enter the string : ")
#fo.append(str1)
fo.write(str1)
fo.close()
fo=open("data1.txt","r")
str2=fo.read(1000)
print(str2)
fo.close()


#%%
#3. Program to read a file line by line and store it into a list
fo=open("a.txt","r")
str1=fo.read(500)
l=str1.split('.')
print(l)
fo.close()


#%%
#4. Program to find the longest word.
with open('a.txt','r') as f:
    data=f.read()
    l=data.split()
    d={}
    count=0
    d={i:len(i) for i in l}
    for i in d:
        if(d[i]>count):
            count=len(i)
            str2=i
    print("Longest word : ",str2)
    f.close()


#%%
#5. Program to combine each line from first file with the corresponding line in second file
with open('data.txt','r') as f1:
    a=f1.read()
    l1=a.split('.')
    with open('data1.txt','r') as f2:
        b=f2.read()
        l2=b.split('.')
        i=0
        if len(l1)>len(l2):    
            while(i!=len(l2)-1):
                print(l1[i])
                print(l2[i])
                i+=1
            while(i!=len(l1)-1):
                print(l1[i])
                i+=1
        else:
            while(i!=len(l1)-1):
                print(l1[i])
                print(l2[i])
                i+=1
            while(i!=len(l2)-1):
                print(l1[i])
                i+=1
    f2.close()
f1.close()


#%%
#6. Average of each line from the file and display it seperately in a dictionary
with open("data3.txt","w+") as f:
    for i in range(5):
        str1=input("Enter string...")
        if i==0:
            f.write(str1)
        else:
            f.write("\n"+str1)
f.close()      
with open("data3.txt","r+") as f:
    data=f.read()
    l1=data.split('\n')
    l2=[]
    for i in l1:
        l2.append(len(i))
    l3=[]
    for i in l1:
        str2=i.split()
        count=0
        for j in str2:
            count+=1
        l3.append(count)
print(l1)
print(l2)
print(l3)
d={}
for i in range(len(l1)):
    d[(l1[i],l2[i])]=l2[i]/l3[i]
print(d)


#%%
#7. Average of each year seperately and show it seperately yearwise in a dictionary
with open("d.txt","r+") as d1:
    a=d1.read(300)
    d={}
    l=a.split('\n')
    for i in l:
        l1=[]
        a=i.split(',')
        count=0
        s=int(a[1])+int(a[2])+int(a[3])+int(a[4])
        s=s/4
        d['Average of year ',a[0]]=s
    print(d)
  
      
#%%
#8. Program to get the file size of a plain file
import os
fs=os.stat("data3.txt")
print(fs)
print("File Size... ",fs.st_size)


#%%
#9. Program to write a list to a file
with open("data3.txt","a+") as f:
    l=["advv","abc","operating","fasd"]
    for i in l:
        f.write(i+"\n")
    f.close()
with open("data3.txt","r+") as f:    
    str1=f.read()
    print(str1)
    f.close()
    
    
#%%
#10. Program to remove newline characters from a file
with open("data3.txt","w+") as f:
    for i in range(5):
        str1=input("Enter string...")
        f.write(str1+"\n")
f.close()      
print("File read...")  
with open("data3.txt","r+") as f:
    str1=f.read()
    l=str1.split('\n')
    print(str1)
f.close()
with open("data3.txt","w+") as f:
    for i in l:
        f.write(i+" ")
f.close()

print("New file...")
with open("data3.txt","r+") as f:     
    str2=f.read()
    print(str2)
f.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

















