import numpy as np
# a1 = np.random.random((3,3)) 
# b1 = np.round(a1*100)    # round means make round figure

# print(a1)
# print(b1)
# print(b1.dtype)

########### mathematical operations ########## -  np.max/min/sum/products()
###syntax: np.max/min/sum/products(a)
###syntax: np.max/min/sum/products(a,axis=0/1) - for column/row wise operation

# x = np.arange(0,10).reshape(5,2)
# print(x)

# print(np.max(x))     # np.max() : to find the max item in an array

# print(np.max(x,axis=0)) # column-wise max

# print(np.max(x, axis= 1)) # row-wise max

# print(np.min(x))   #np.min : to find the min item in an array

# print(np.sum(x))   #np.sum : to find the sum of items in an array

# print(np.prod(x))   #np.prod : to find the products of all items in an array


#####.................  0 = column-wise, 1 = row-wise

# print(np.max(b1, axis=0))     #column wise maximum items

# print(np.max(b1, axis=1))   #row wise maximum items


################## stastical operations ############### --  np.mean/median/std/var()
### syntax: np.mean/median/std/var(a)
### syntax: np.mean/median/std/var(a,axis=0/1)

# y = np.arange(1,11)
# print(y)
# z = np.arange(1,10)
# print(z)

# print(np.mean(y))            #mean - gor-(average)

# print(np.median(z))          # median (middle number in a data set)

# print(np.std(y))             #std - standard deviation [have to understand std]

# print(np.var(b1, axis=0))    #var - variance [have to understand var], (here column wise)


################## trigonometry function ############ - it usually not use in data science
##syntax: np.sin/cos/tan...(a)

# print(np.sin(b1))
#...


############### dot product ############### - matrix dot multiplication - example:(2*3).(3*2)
## syntax: np.dot(a,b)

# m = np.arange(12).reshape(3,4)
# n = np.arange(12,24).reshape(4,3)
# print(m)
# print(n)

# print(np.dot(m,n)) # dot product - matrix dot multiplication


########### log and exponents #############
## syntax: np.log/exp(a)

# print(np.log(m))       # find the log of each items

# print(np.exp(n))      #find the exponent of each items


############## np.round/floor/ceil() #############
### syntax: np.round/floor/ceil(a)

# r = np.random.random((2,3))*100
# print (r)

# print(np.round(r)) # np.round : making round figuare of each items , ex: 6.5 = 7,   6.4 = 6

# print(np.floor(r)) # np.floor : making floor of each items , ex: 6.9 = 6 (removes the fractional part)

# print(np.ceil(r)) # np.ceil : making ceil of each items , ex: 6.1 = 7

