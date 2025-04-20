import numpy as np


a1 = np.arange(10)  #1D
a2 = np.arange(12,dtype=float).reshape(3,4) #2D
a3 = np.arange(8).reshape(2,2,2)   #3D / tencer   , (2,2,2) here first 2 is the number of 2D array and the rest are number of row,coulmn

# print(a1)
# print(a2)
# print(a3)

############## .ndim ########## - to find the number of dimension (D) of a given array
### syntax: a.ndim

# print(a2.ndim)   # find the number of dimension (D) of a given array

############# .shape ############ - to find the (shape)- number of row/column in a given array
### syntax: a.shape

# print(a1.shape)   
# print(a2.shape)
# print(a3.shape)      

######### .size ######### - to find the number of items in an array
### syntax: a.size
                          
# print(a2.size)      #find the number of items in an array , here (3*4) = 12
# print(a3.size)

######### .itemsize ########## - to find the number of (bytes) are occupied in memory(RAM) by each item in an array
### syntax: a.itemsize

# print(a2.itemsize) 

######### np.int8/16/32/64 ########### - to set data type(bit wise) for the each item
### syntax: dtype= np.int32

# b1 = np.arange(10, dtype= np.int32) # here we initialize int data type of each item which contain 32 bits
# print(b1.itemsize) # 32 bits = 4 (bytes)

##### .dtype ########### -- to find the data type(bit wise) of a given array
### syntax: a.dtype

# print(a1.dtype) 
# print(b1.dtype) 
print(a3.dtype)

############ .astype() ######## - to change the data type(bit wise) of an array- same as - dtype= np.int32
### syntax: a.astype(np.int16)

# c1 = a3.astype(np.int32) 
# print(c1.dtype)