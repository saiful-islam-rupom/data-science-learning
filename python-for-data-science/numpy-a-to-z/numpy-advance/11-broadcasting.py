import numpy as np
###### broadcasting ############

#------- addition between same shape

# a = np.arange(6).reshape(2,3)
# b = np.arange(6,12).reshape(2,3)

# c = a+b
# print(a)
# print(b)
# print(c)

#------- addition between different shape- using broadcasting

# a = np.arange(6).reshape(2,3)
# b = np.arange(3)

# c = a+b
# print(a)
# print(b)
# print(c) # operation occured successfully because of broadcasting, the smaller array "broadcast" across the larger array

#----another examples

# p = np.arange(12).reshape(4,3)
# q = np.arange(3)
# print(p)
# print(q)
# print(p+q) # broadcasting successful

#------another example-- error (unsuccessful)

# p= np.arange(12).reshape(3,4)
# q = np.arange(3)
# print(p+q) # unsuccessful

#-------- another example

# r = np.arange(3).reshape(1,3)
# s = np.arange(3).reshape(3,1)

# print(r)
# print(s)

# print(r+s) # broadcasting successful

#-------another example

# t = np.arange(3).reshape(1,3)
# u = np.arange(4).reshape(4,1)

# print(t+u) # successful

#---------another example

# v = np.arange(1).reshape(1,1)
# w = np.arange(4).reshape(2,2)

# print(v+w) #success

#------another example-- error

# x = np.arange(12).reshape(3,4)
# y = np.arange(12).reshape(4,3)

# print(x+y)   #unsuccess

#-----another example----- error

# a = np.arange(16).reshape(4,4)
# b = np.arange(4).reshape(2,2)

# print(a+b) # unsuccess


