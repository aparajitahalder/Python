# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 06:42:29 2019

@author: Aparajita
"""


#%%
import numpy as np

a=np.array([1,2,3])
a
type(a)
print(a.shape)
print(a[0],a[1],a[2])
a[0]=5
a
b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,1],b[0,2])
print(b)


#%%
a=np.zeros((3,2))
a
b=np.ones((4,4))
b
c=np.full((3,4),11)
c
d=np.eye(3)
d
e=np.random.random((3,5))
e


#%%
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
b=a[:1,1:2]
b
print(a[1,2])
b[0,0]=70
print(a[0,1])


#%%
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
row_r1 = a[1, :]   # Rank 1 view of the second row of a
row_r2 = a[1:2, :]   # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)   # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)   # Prints "[[5 6 7 8]] (1, 4)"
col_c1=a[:,1]
col_c2=a[:,1:2]
print(col_c1,col_c1.shape)
print(col_c2,col_c2.shape)


#%%
a=np.array([[1,2],[3,4],[5,6]])
print(a[[0,1,2],[0,1,0]])
print(np.array([a[0,0],a[1,1],a[2,0]]))
print(a[[0,0],[1,1]])
print(np.array([a[0,1],a[0,1]]))


#%%
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
b=np.array([0,0,0,1])
print(b)
print(a[np.arange(4), b])
a[np.arange(4),b]+=1
print(a)


#%%
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
b=a>2
print(b)
print(a[b])
print(a[a>2])


#%%
x=np.array([1,2])
print(x.dtype)
x=np.array([1.2,2.4])
print(x.dtype)
x=np.array([1.2,2.4],dtype="int64")
print(x.dtype)
print(x)


#%%
x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print(x+y)
print(np.add(x,y))
print(np.sqrt(x))


#%%
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
v=np.array([9,10])
w=np.array([11,12])
print(v.dot(w))
print(np.dot(v,w))
print(x.dot(y))
print(np.dot(x,y))


#%%
x=np.array([[1,2],[3,4]])
print(np.sum(x))   #compute sum of all elements
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))


#%%
x=np.array([[1,2],[3,4]])
print(x)
print(x.T)


#%%
x=np.array([[1,2,3],[4,5,6],[7,8,9],[11,12,13]])
v=np.array([1,0,1])
y=np.empty_like(x)
for i in range(4):
    y[i,:]=x[i,:]+v
print(y)


#%%
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
v=np.array([1,0,1])
vv=np.tile(v,(3,1))
print(vv)
y=x+vv
print(y)


#%%
import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
y=x+v
print(y)


#%%
v=np.array([1,2,3])
w=np.array([4,5])
print(np.reshape(v,(3,1))*w)
x=np.array([[1,2,3],[4,5,6]])
print(x+v)
print((x.T+w).T)
print(x+np.reshape(w,(2,1)))
print(x*2)















