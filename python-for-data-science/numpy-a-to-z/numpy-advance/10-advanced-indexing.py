import numpy as np

############ fancy indexing ######### - when you have to get unpatterned array items

# a = np.arange(12).reshape(4,3)
# print(a)

# print(a[[0,2,3]]) # to get 1st,3rd and 4th rows

# b = np.arange(24).reshape(6,4)
# print(b)

# print(b[:,[0,2,3]]) # to get 1st,2nd and 4th column

################# boolean indexing #############-using different conditions - (T/F)

# a = np.random.randint(1,100,24).reshape(6,4) # here- in- randint(1st number, last number, how many number)
# print(a)
#???????????????? find all number greater than 50

# print(a>50) # boolean indexing - (T/F)
# print(a[a>50]) # filtering and get the desired items using boolean indexing as boolean mask

#???????????? find out even numbers

# print(a % 2 == 0) # boolean indexing based on condition
# print(a[a % 2 == 0]) # filtering using boolean indexing

#???????????????? find out the even numbers that and greater than 50 (two conditions)

# print((a>50) & (a % 2 == 0)) #boolean indexing based on condition
# print(a[(a>50) & (a % 2 == 0)]) #filtering using boolean indexing as mask

#???? find all the numbers that are divisable by 7

# print(a % 7 == 0) # boolean indexing
# print(a[a % 7 == 0]) # filtering using booling indexing

#?????????? find all numbers that are not divisable by 7

# print(a[a % 7 != 0])
# print(a[~(a % 7 == 0)]) # -alternative way

