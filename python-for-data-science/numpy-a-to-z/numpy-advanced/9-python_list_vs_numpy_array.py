
############ speed test- python vs numpy ##############

#----- speed of python list -----------
# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]
# c = []

import time

# start = time.time()

# for i in range(len(a)):
#     c.append(a[i]+b[i])

# print(time.time()-start)

#------------- speed of numpy array----------
import numpy as np

# e = np.arange(10000000)
# f = np.arange(10000000,20000000)

# start = time.time()
# g = e+f
# print(time.time()-start)

# print(0.962/0.018) #numpy array is 53.44X faster than python list

################# memory test - python vs numpy #######################

import sys
#---------- memory occupied by pyhon list ---------
# x = [i for i in range(10000000)]  

# print(sys.getsizeof(x))  # size of the phython list-- output is in byte form

#--------- memory occupied by numpy array ----------
# y = np.arange(10000000)
# print(sys.getsizeof(y))  # size of the numpy array --- output is in byte form

# z = np.arange(10000000, dtype=np.int32) # numpy array gives the size flexibility
# print(sys.getsizeof(z))

#------#---- numpy array is much more convenient than python list-----#------------#