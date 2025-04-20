### characteristics of set:
#1. unique values/elements/items
#2. unordered - no indexing
#3. mutable - add/remove elements
#4. immutable elements- elements can not be changed or modified or replaced


#### creating set ####

# set1 = {1,2,3,"ddkg",True}
# print(set1)

# m_set = set([1,2,3,4])
# print(m_set)

# empty_set = set() #to create empty set
# print(empty_set)

######### set operation  ######## - only add and remove

# fruits = {'apple','banana'}
# fruits.add('cherry')          #add - set object has no attribute 'append'
# print(fruits)

# fruits.remove('banana')   #remove - if element is not found to remove it, shows error
# print(fruits)

# fruits.discard('afule')   #discard - if element is not found to remove it, doesn't shows error
# print(fruits)

###### set methods -4 ######
### 1. union ### - combine elements of two sets, romoving duplicates

# set1 = {1,2,3}
# set2 = {3,4,5}
# u_set = set1.union(set2)  # s1.union(s2)
# print(u_set)
# u_set2 = set1 | set2  #alternative method
# print(u_set2)

### 2. intersection #### - Includes only elements in both sets
# set1 = {1,2,3,4}
# set2 = {3,4,5}
# inter_set = set1.intersection(set2)
# print(inter_set)
# inter_set2 = set1 & set2  #alternative method
# print(inter_set2)

### 3. difference ### - elements present in the first set but not in the second
# set1 = {1,2,3,4}
# set2 = {3,4,5}
# diff_set = set1.difference(set2)
# print(diff_set)
# diff_set2 = set1 - set2  #alternative method
# print(diff_set2)

### 4. symmetric difference ### - elements in either set but not in both
# set1 = {1,2,3,4}
# set2 = {3,4,5}
# sdiff_set = set1.symmetric_difference(set2)
# print(sdiff_set)
# sdiff_set2 = set1 ^ set2  #alternative method
# print(sdiff_set2)

##### set iteration #####
### using for loop ###

# setx = {1,2,3,4,5,6}
# for i in setx:
#     print(i)

### using while loop ### -while loop can not be used for set directly, to use , convert set -> list and then use while loop


##### set comprehension #### - (similar to list)
### syntax: my_set = {expression 'for' item 'in' iterable 'if' condition}

# squares_set = {x**2 for x in range(1,6)}
# print(squares_set)