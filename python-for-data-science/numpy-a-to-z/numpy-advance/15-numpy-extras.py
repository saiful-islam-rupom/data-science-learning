import numpy as np
################################## some useful numpy functions #################################

##### np.sort()  ######## - for sorting - ascending/discending

# a = np.random.randint(1,100,15)
# b = np.random.randint(1,100,15).reshape(5,3)

# print(a)
# print(b)

# print(np.sort(a))             # ascending sort for 1D array
# print(np.sort(a)[::-1])         # discending sort for 1D array

# print(np.sort(b))         # row wise ascending sort for 2D array

# print(np.sort(b,axis=0)) # column wise ascending sort for 2D array (column wise = 0 , row wise = 1)

################ np.append() ######### for append

# print(np.append(a,200))             # append in 1D array
# print(np.append(a,[200,202]))       # 1D append
# print(np.append(a,range(200,211))) # 1D append
# print(np.append(a,np.arange(200,211)))  # 1D append -same as above

# print(np.append(b,np.ones((5,1)),axis=1)) # append column(row wise append), so axis = 1
# print(np.append(b,np.ones((b.shape[0],1)),axis=1)) # same as above but append based on shape of the array(b)

############## np.concatenate() ###### alt---------stack
### syntax: np.concatenate((a,b), axis= 0/1)

# c = np.arange(6).reshape(2,3)
# d = np.arange(6,12).reshape(2,3)
# print(c)
# print((d))
# print(np.concatenate((c,d), axis=0) ) #column wise concatenate / vertical concatenate, axis=0
# print(np.concatenate((c,d), axis=1) ) #row wise concatenate / horizontal concatenate, axis=1

############# np.unique() ########### ------------ to get unique items in array
### syntax: np.unique(a)

# a = np.array([1,1,1,2,2,3,4,4,5,5,5,6,6,9,99,99])

# print(np.unique(a)) # to get unique items and (remove duplicates)

################## np.expand_dims() ############### - expand dimention
### syntax: np.expand_dims((a),axis=0/1)

# a = np.arange(10)
# print(a)

# print(np.expand_dims((a),axis=0)) # axis=0 makes it horizontal array
# print(np.expand_dims((a),axis=1))  # axis=1 makes it vertical array

############ np.where() ############## - to find the "index position" of items based on the condition
#### syntax: np.where(condition)
#### syntax: np.where(condition,true,false)  -filtering- This function returns elements chosen from x/true or y/false, depending on the condition.

# a = np.random.randint(0,20,10)
# print(a)

# print(np.where(a>10)) 

# print(np.where(a>10,0,a)) # convert into 0 ,which items are greater than 10
# print(np.where(a>10,0,99)) # convert into 0,which items are greater than 10 otherwise convert into 99

####### np.agrmax() / np.argmin() ######- to find the index position of max/min value in an array
### syntax: np.argmax/min(a)
### syntax: np.argmax/min(b,axis=0/1)

# print(np.argmax(a)) # to find the index position of max value in an array

# b = np.random.randint(0,101,24).reshape(6,4)
# print(b)
# print(np.argmax(b)) #for 2D, find the index positon(serial wise/ treat as 1D) which contains max value

# print(np.argmax(b,axis=0)) #for 2D, column wise max values- index position
# print(np.argmax(b,axis=1)) #for 2D, row wise max values- index position

# print(np.argmin(a)) # opposite of np.argmax()

######### np.cumsum() ################ --- cumulative sum
#### syntax: np.cumsum(a)
#### syntax: np.cumsum(b,axis=0/1)

# print(np.cumsum(a)) # to find cumulative sum

# print(np.cumsum(b)) # if axis is not specified in 2D, than it will make it 1D
# print(np.cumsum(b,axis=0)) # in 2D , coulum wise cumsum
# print(np.cumsum(b,axis=1)) # in 2D , row wise cumsum

####### np.cumprod() ################# ---- cumulative product - as like as cumsum
#### syntax: as like as np.cumsum()

# print(np.cumprod(a)) 

########## np.percentile() ##########
### syntax: np.percentile(a,percent)

# print(np.percentile(a,100)) # ---- the biggest
# print(np.percentile(a,99)) 
# print(np.percentile(a,0))  # --------- the smallest
# print(np.percentile(a,50)) # ------ the median

###### np.histogram() ########## -- frequency count for a given bin
### syntax: np.histogram(a,bin=[x,y,z])

# a = np.random.randint(0,51,10)
# b = np.array([9,12,12,23,24,34,45,46,47,57])

# print(a)
# print(b)

# print(np.histogram(a,bins=[0,10,20,30,40,50])) # histogram, frequency count for a given bin
# print(np.histogram(b,bins=[20,30,40,50,60,70]))

######## np.corrcoef() ########## - corelation coefficient - 
### syntax: np.corrcoef(a,b)

# salary = np.array([15000,20100,25000,30100,35200])
# exp = np.array([1,2,3,4,5])

# print(np.corrcoef(salary,exp)) # corelation


######### np.isin() ############ to search(T/F) single/multiple(anyone) items in an array in same time 
### syntax: np.isin(a,item)
### syntax: np.isin(a,[item,item,item])

# a = np.random.randint(0,101,50)
# items = np.array([10,20,30,40,50,60,70,80,90,100])
# print(a)


# print(np.isin(a,items))  # T/F
# print(np.isin(a,[10,20,30,40,50,60,70,80,90,100])) # same as above
# print(np.isin(a,33))

# print(a[np.isin(a,items)]) # -filtering- to get the items from array

############# np.flip() ######### --to reverse / flip
### syntax: np.flip(a)
### syntax: np.flip(a,axis=0/1)

# a = np.random.randint(0,20,10)
# print(a)

# print(np.flip(a)) # make reverse

# b = np.random.randint(0,24,12).reshape(4,3)
# print(b)
# print(np.flip(b)) # for 2D array, it flip both row and column wise

# print(np.flip(b,axis=0)) # for 2d, column wise flip

############ np.put() ############### - put values in an array {parmanently} using index 
### syntax: np.put(a,[index,index...],[value,value...])

# a = np.array([10,20,30,40,50])
# print(a)
# np.put(a,[0,2],[100,300])
# print(a)

############ np.delete() ######## to delete items using index
### syntax: np.delete(a,[index,index...]) 

# a = np.array([2,3,4,5,6,7,8,9])
# print(a)

# print(np.delete(a,[0,1]))

######### Set functions ##########
# a = np.array([1,2,3,4,5])
# b = np.array([3,4,5,6,7,8,9,10])

### np.union1d() ###
# print(np.union1d(a,b)) # union - all including common and uncommon (don't include extra duplicates)

### np.intersect1d() ###
# print(np.intersect1d(a,b)) # intersection - only commons

### np.setdiff1d() ####
# print(np.setdiff1d(a,b)) # set diff- items that are in a but not in b,   uncommons of set a 

#### np.setxor1d() ####
# print(np.setxor1d(a,b)) #set xor - remove the commons / opposite of intersection


############ np.clip() ####### - - to set limit/restrict/range on the items {do not remove items}
### syntax: np.clip(a,a_min=x,a_max=y)

# a = np.random.randint(0,501,20)
# print(a)
# print(np.clip(a,a_min=100,a_max=200))

############## np.swapaxes() ########## - make row as column and column as row
#### syntax: np.swapaxes(a,0,1)

# a = np.random.randint(0,100,24).reshape(6,4)
# print(a)

# print(np.swapaxes(a,0,1)) #to make row as column and column as row
# print(np.swapaxes(a,1,0)) # same as above


########## np.random.uniform() #########-- generates random floating-point numbers from a uniform distribution within a specified range
## A uniform distribution means that every value within a given range has an equal probability of being selected.
### syntax: np.random.uniform(low, high, how many)

# a = np.random.uniform(1,10,3) 
# print(a)

############ np.count_nonzero() ######### - to count {how many} items are nonzero

# a = np.array([1,3,0,6,2,0,4,0,3])
# print(np.count_nonzero(a))

########### np.title() ########### --- to add/append a copy with existing array- 
### syntax: np.title(a,how many copy)

# a = np.array([1,2,3])
# print(np.tile(a,3)) 

########## np.repeat() ########## -- to repeat items --
### syntax: np.repeat(which item, how many)

# print(np.repeat(3,4))

# a = np.repeat(5,5)
# print(a)

# b = np.array([1,2,3])
# print(np.repeat(b,3)) # to repeat each item how many times of an arry

########### np.allclose() ########-- it is used to check whether two arrays are element-wise "close enough" within a given tolerance.\n
#-It returns True if all elements in a and b are approximately equal; otherwise, it returns False
### syntax: np.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
###----[[confusion]] --{{Have to understand theory and code-syntax}}


######## np.equal() ############# -- to see the items(specified) are equal or not {index wise} in an array (T/F)
### syntax: np.equal([x,y,z],a)

# a = np.array([1,2,3])
# print(np.equal([3,4,3],a))
