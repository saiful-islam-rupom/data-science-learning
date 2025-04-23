import numpy as np

############### indexing ##################
# a = np.arange(10)
# print(a)
# print(a[0]) # 1D array indexing
# print(a[5])

b = np.arange(12).reshape(3,4)
print(b)
print(b[1])
# print(b[1,2]) # 2D array indexing- syntax: a[row,column] -; here 1 is the position of row and 2 is the position of column

# c = np.arange(12).reshape(2,3,2)
# print(c)
# print(c[1,0,1]) # 3D array indexing - syntax: a[position of 2D array,row,column] ; here first number is the position of 2D array, and rest are as same as 2D array indexing

#################### slicing #########################

# print(a)
# print(a[3:6]) #1D array slicing -syntax: a[start:end] ; here, slice of 3,4,5 - same as python slicing

# print(b)

# print(b[1,:]) # 2D array slicing- - slice of second row 4,5,6,7
# print(b[:,2]) # 2D array slicing - slice of third column 2,6,10
# print(b[1:,1:3]) #2D array slicing - slice of 5,6 \n 9,10
# print(b[::2,::3])  #2D array slicing - slice to get the values of four corner
# print(b[::2,1::2]) # 2D array slicing - slice of 1,3 and 9,11

# print(b[1:2,::3]) # 2D - slice of [4 7] - it works but it creates a 2D slice
# print(b[1,::3]) # 2D -slicice of [4 7]

# d = np.arange(27).reshape(3,3,3)
# print(d)

# print(d[1]) # 3D array slicing - slice of second 2D array
# print(d[1,:,:]) # 3D array slicing - same as above

# print(d[::2]) # 3D - slice of first and third 2D array
# print(d[::2,:,:]) # 3D - same as above

# print(d[0,1,:]) # 3D - slice of 2nd row of 1st 2D array in 3D array
# print(d[1,:,1:2]) # 3D - slice of second column of second 2D array in 3D array -- this is to get original shape
# print(d[1,:,1]) # 3D - same as above -- this is to get normal shape

# print(d[2,1:3,1:3]) #3D- slicing
# print(d[2,1:,1:]) # 3D - same as above

# print(d[::2,0,::2]) #3D- slicing





