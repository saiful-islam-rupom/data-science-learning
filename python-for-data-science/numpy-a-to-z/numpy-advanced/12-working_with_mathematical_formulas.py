import numpy as np
###### creating own mathematical functions ########

######### sigmoid ###########
# def sigmoid (array):
#     return 1/(1+np.exp(-(array)))

# a = np.arange(10)
# print(sigmoid(a))

####### mean squared error ######## - loss function im ML

# actual = np.random.randint(1,50,25)
# predicted = np.random.randint(1,50,25)

# print(actual)
# print(predicted)

# def mse(act,pre):
#     return np.mean((act - pre)**2)
##    return (np.sum(((act - pre)**2))) / len(actual)    # alternative
##    return (np.sum(((act - pre)**2))) / 25             # alternative

# print(mse(actual,predicted))

######### binary cross entrophy ##### _ loss function in ml (HW) (confusion)

# actual = np.random.randint(0,2,25)
# print(actual)
# predicted = np.random.randint(0,2,25)
# print(predicted)

# def bce(act,pre):
#     return -np.mean(act * np.log(pre) + (1 - act) * np.log(1 - pre))

# print(bce(actual,predicted))

# def bce(act,pre): # this is may be an alternative
#     return -(np.sum((actual * np.log(predicted)) + (1 - actual) * np.log(1 - predicted)))/ len(actual)

# print(bce(actual,predicted))