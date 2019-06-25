# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:30:18 2019

@author: Aparajita
"""
#%%
#1 No. between 1500-2701 and multiple of 5 and divisible by 7 
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print("  ",i)
#%%        
#2 PATTERN_1
print("PATTERN.......")
k=5
for i in range(12):
    if i<=5:
        for j in range(i+1):
            print(" * ",end="")
        print("\n")
    elif i>5 :
        for j in range(k+1):
            print(" * ",end="")
        print("\n")
        k=k-1
    
#%%        
#3 REVERSE WORD
a=int(input("ENTER THE WORD : "))
while(a>=1):
    b=a%10
    print(int(b),end="")
    a=a/10
s=input("ENTER THE WORD : ")   
print(s[::-1])

#%%
#4 Print all no. from 0-6 except 3 and 6
print("\n")
for i in range(7):
    if(i!=3 and i!=6):
        print(i,end=" ")
    continue
        
#%%
#5 Binary no. accepting ','
value = []
items=[]
a=int(input("How many no.s you want to enter : "))
for i in range(a):
    a=input()
    items.append(a)
for p in items:
    d = int(p, 10)
    if d%5:
        value.append(p)

print(value)
    
#%%
#6 Print Pattern A
print("\n")
for i in range(1,8):
    for j in range(1,6):
        if i==1:
           if j==2 or j==3 or j==4:
               print("*",end="")
           else:
               print(" ",end="")
        elif i==4:
               print("*",end="")
        else:
           if j==1 or j==5:
               print("*",end="")
           else:
               print(" ",end="")
    print("")

#%%
#7 VOWEL OR CONSONANT
a=input("ENTER THE ALPHABET : ")
if a=='a' or a=='A' or a=='E' or a=='e' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U' :
    print("ALPHABET IS VOWEL")
else :
    print("ALPHABET IS CONSONANT")
    
#%%    
#8 PRINT MONTH AND DAY
d=int(input("ENTER THE DAY : "))
m=int(input("ENTER THE MONTH : "))
if m<1 and m>12:
    print("WRONG INPUT")
elif m>=3 and m<=4:
    if m==3 and d>=3 :   
       print(d,"/",m," is SPRING SEASON")
    elif m==3 and d<3 :   
       print(d,"/",m," is WINTER SEASON")
    else:
       print(d,"/",m," is SPRING SEASON")
        
elif m<=2 and m>=11:   
       print(d,"/",m," is WINTER SEASON")
elif m>=5 and m<=8:
   if m==5 and d>=5 :   
       print(d,"/",m," is SUMMER SEASON")
   elif m==5 and d<5 :   
       print(d,"/",m," is SPRING SEASON")
   else:
       print(d,"/",m," is SUMMER SEASON")
    
elif m>=9 and m<=10:
    if m==9 and d>=5 :   
       print(d,"/",m," is RAINY SEASON")
    elif m==9 and d<5 :   
       print(d,"/",m," is SUMMER SEASON")
    else:
       print(d,"/",m," is RAINY SEASON")
    
       
#%%
#9 STRING INTEGER OR NOT
a=input("ENTER THE STRING : ")
b=str.isdigit(a)
if b==0:
    print("STRING NOT INTEGER")
else:
    print("STRING IS INTEGER")
    
#%%
#10 SUM OF TWO NO. AND RETURN 20 if sum between 15 and 20 
a=int(input("ENTER FIRST NO. : "))
b=int(input("ENTER SECOND NO. : "))
c=a+b
if c>=15 and c<=20:
    print("SUM IS : ",20)
else:
    print("SUM IS : ",c)
#%%
#11 PATTERN S
for i in range(1,8):
    for j in range(1,6):
        if i==1:
            if j==1:
                print(" ",end="")
            else:
                print("*",end="")
        elif i==2 or i==3:
            if j==1:
                print("*",end="")
            else:
                print(" ",end="")
        elif i==4:
             if j==1 or j==5:
                print(" ",end="")
             else:
                print("*",end="")
        elif i==5 or i==6:
            if j==5:
                print("*",end="")
            else:
                print(" ",end="")
        elif i==7:
            if j==5:
                print(" ",end="")
            else:
                print("*",end="")
        
            
    print("")

#%%
#12 TABLE OF A NUMBER
y=int(input("ENTER FIRST NO. : "))
for i in range(1,11):
    print("\n",i,"*",y,"=",i*y)

     
#%%    
#13 PATTERN S
for i in range(1,16):
    for j in range(1,16):
       if i==4 or i==5 or i==6:
           if j==1 or j==2 or j==3:
               print("o",end="")
           else :
               print(" ",end="")
       elif i==10 or i==11 or i==12:
           if j==13 or j==14 or j==15:
               print("o",end="")
           else :
               print(" ",end="")
       else:
           print("o",end="")
    print("")
        

#%%
#14 NEXT DAY OF GIVEN DATE 
d=int(input("ENTER THE DAY : "))
m=int(input("ENTER THE MONTH : "))
y=int(input("ENTER THE YEAR : "))
 
if ((y % 4 == 0) and (y % 100!= 0)) or (y%400 == 0):
    if m==2:
        d1=29
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        d1=31
    else :
        d1=30
else:
    if m==2:
        d1=28
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        d1=31
    else :
        d1=30

if d==31 and m==12 :
    d=1
    m=1
    y=y+1   
elif d1-d==0 :
    m=m+1
    d=1
else:
    d=d+1
    
print("NEXT DAY IS : ",d,"/",m,"/",y)

#%% 
#15 2D Matrix
m=int(input("ENTER THE ROWS : "))
n=int(input("ENTER THE COLUMNS : "))
for i in range(1,m+1):
     for j in range(1,n+1):
         print(i*j,end="  ")
     print("\n")
    
#%%

    






