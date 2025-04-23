import numpy as np

######## stacking ##########
b = np.arange(12).reshape(3,4)
c = np.arange(12,24).reshape(3,4)
# print(b)
# print(c)
d = np.arange(24,36).reshape(3,4)
# print(d)

# print(np.hstack((b,c)))     # horizontally stacking - syntax:  np.hstack(a,b,c)

# print(np.vstack((b,c,d)))   # vertically stacking - syntax: np.vstack(a,b,c)

############### splitting ##################

# print(np.hsplit(b,2))  # np.hsplit - horizontally splitting
# print(np.vsplit(b,3))  # np.vsplit - vertically splitting



