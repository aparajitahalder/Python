# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 03:48:33 2019

@author: Aparajita
"""
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
    
    
#8 PRINT MONTH AND DAY
d=int(input("ENTER THE DAY : "))
m=int(input("ENTER THE MONTH : "))
if m<1 and m>12:
    print("WRONG INPUT")
if m>=11 or m<=2:
    print(d,"/",m," is WINTER SEASON")
if m>=3 and m<=4:
    print(d,"/",m," is SPRING SEASON")
if m>=5 and m<=8:
    print(d,"/",m," is SUMMER SEASON")
if m>=9 and m<=10:
    print(d,"/",m," is RAINY SEASON")


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
for i in range(1,6):
     for j in range(1,6):
         print(i*j,end="  ")
     print("\n")
    
#%%
    
    
    
#%%
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










