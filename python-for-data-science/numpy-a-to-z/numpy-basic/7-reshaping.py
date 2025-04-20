import numpy as np

########### .reshape() #######
#----------------already learned

########## np.transpose() ############# - make the matrix's row as column and column as row
### syntax: np.transpose(a)
### syntax: a.T

b = np.arange(12).reshape(3,4)
# print(b)

# print(np.transpose(b)) # np.transpose - transpose
# print(b.T) # alternative way - transpose

########### np.ravel() ######### - make 2D,3D... into 1D array
### syntax: np.ravel(a)
### syntax: a.ravel()

# print(np.ravel(b)) # ravel 
# print(b.ravel()) # alternative way - ravel 

