# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

#FIND ODD EVEN NUMBER
a=int(input("ENTER A NO. : "))
if (a%2==0) :
    print("No. is even...")
else:
    print("No. is Odd...")
#%% 

#LARGEST OF THREE NUMBERS
a=int(input("ENTER FIRST NO. : "))
b=int(input("ENTER SECOND NO. : "))
c=int(input("ENTER THIRD NO. : "))
if a > b:
    if a>c:
        print(a, "is greater")
    elif b>c:
        print(b, "is greater")
else :
    print(c, "is greater")
#%%

#TABLE OF A NUMBER
y=int(input("ENTER FIRST NO. : "))
for i in range(1,11):
    print("\n",i,"*",y,"=",i*y)


#%%

#FACTORIAL OF A NUMBER
a=int(input("ENTER FIRST NO. : "))
b=1
while(a>1):
    b=b*a
    a=a-1
print("FACTORIAL OF NUMBER : ",b)
#%%

#Fibbonacci SERIES
f1=0
f2=1
a=int(input("ENTER THE NUMBER YOU WANT THE SERIES UPTO : "))
print("SERIES.....")
print("\n",f1,"\n",f2)
while(a>2):
     f3=f1+f2
     f1=f2
     f2=f3
     print("\n",f3)
     a=a-1






