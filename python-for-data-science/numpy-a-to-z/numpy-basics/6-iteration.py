import numpy as np
######### iteration in array ##########
a1 = np.arange(10)

# for i in a1:   #1D - item wise iteration
#     print(i)

a2 = np.arange(12).reshape(3,4)
# print(a2)
# for i in a2:  #2D - row wise iteration
#     print(i)

a3 = np.arange(12).reshape(3,2,2)
# print(a3)
# for i in a3:   #3D -  2D_array wise iteration
#     print(i)

###### np.nditer() ###### to iter each items in 2D, 3D,... array 
### syntax: np.nditer(a) 

# for i in np.nditer(a3):  
#     print(i)
