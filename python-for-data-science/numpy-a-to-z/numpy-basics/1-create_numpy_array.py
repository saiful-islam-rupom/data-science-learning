

import numpy as np

########## creating numpy array ############

# a = np.array([1,2,3])  #1D numpy array/vector
# print(type(a))
# print(a)

# b = np.array([[1,2,3],[4,5,6]]) #2D numpy array/Matrix
# print(b)

# c= np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #3D numpy array/tencer
# print(c)

# p = np.array([1,2,3] , dtype=float) #difining data type of an array
# print(p)
# q = np.array([1,0,3] , dtype=bool)
# print(q)


########### np.arange() ######### -similar as python range- 
## syntax: np.arange(start,end,step)
r=np.arange(1,11)
# print(r)

# s=np.arange(1,11,2)
# print(s)

####### .reshape() ########- to reshape array (row,column) -1D/2D/3D- 
## syntax1: .reshape(row,column) - to reshape as 2D
## syntax2: .reshape(how many 2D array,row,column) - to reshape as 3D

# m= r.reshape(5,2) #to reshape array (row,column)
# print(m)

# x = np.arange(0,24).reshape(2,3,4)
# print(x)


########## np.ones() ##############- to generate only '1'
## syntax: np.ones((row,column))
# o = np.ones((5,3))
# print(o)

########## np.zeros() ########### - to generate only '0'
## syntax: np.zeros((row,column))
# z= np.zeros((3,2))
# print(z)

########## np.random.Xrandom() ############- to generate random numbers
### syntax: np.random.random((row,column))
### syntax: np.random.randint(start,end,how many number want to print)

# r = np.random.random((3,2))  # generate random numbers between (0 to 1) in the items (for second .random)
# print(r)

# s = np.random.randint(0,10,5)  # generate random intger numbers 
# print(s)

######### np.linspace() ######## to create x number of points with (same distance)
## syntax: np.linspace(fast number,last number,how many points want to create)

# l = np.linspace(-10,10,6) #creating x number of points(same distance)
# print(l)

######## np.identity ########### - to create identity matrix - 2D
## syntax: np.identity(numbers of diagonal "1")

i = np.identity(5) #creating identity matrix
print(i)