### create tuple ####

# tup = (1,2,'saiful',True)
# print(tup)

# tu = 1,2,3,4,'a'
# print(tu)

# tup2 = tuple((12,16,20))    # tuple(()) - make tuple
# print(tup2)

# lst = [1,2,3]
# tup3= tuple(lst)
# print(tup3)

# tup4 = ("a",)   #for single element in tuple
# print(tup4)

### access tuple using indexing ### - same as in "list"

### tuple slicing ### - same as "list" slicing

### tuple operations ###

# tpl = (1,2,3)
# tpl1 = (4,5)

# tp = tpl + tpl1  #concetenation
# print(tp)

# tp1 = tpl * 3  #repetation
# print(tp1)

# tpl3 = (1,2,3,4,5)  
# print(7 in tpl3)        #checking for element in tuple T/F

### iterating over tuple ### - using for and while loop - same as "list"
### using for loop ###

# tx =("Apple","banana","coconut")
# for i in tx:
#     print(i)

# #using while loop

# ty = ("kdfk",12,"kdsjfk",14)
# index = 0
# while index < len(ty):
#     print(ty[index])
#     index += 1


### tuple methods ###------ only two methods

# numbers = (1,5,6,5,3,5,"a", True)
# print(numbers.count(5))   # .count()-- to count desired item
# print(numbers.count("a"))
# print(numbers.count(True))

# print(numbers.index(5))   #find index number


### tuple functions ###

# num= (23,14,56,99)  #length
# print(len(num))

# num= (23,14,56,99,)
# print(sum(num))      #sum of element

# num= (23,14,56,99)
# print(min(num))      #min element

# num= (23,14,56,99)
# print(max(num))      #max element

# num= (23,14,56,99)
# print(sorted(num))      #sort and convert a tuple into list


### tuple packing and unpacking ###

# a = "Saiful"
# b = 24
# c = "Engineer"

# tpl_pack = a,b,c                       # packing
# tpl_pack1 = "Rupom", 23, 23.3            # packing
# print(tpl_pack)
# print(tpl_pack1) 

# name,age,profession = tpl_pack   #unpacking
# print("Name is", name)
# print("Age is", age)
# print("prof is", profession)


### modify tuple ###- tuple can not be modified directly - to modify tuple, convert tuple -> list(modify) -> tuple
