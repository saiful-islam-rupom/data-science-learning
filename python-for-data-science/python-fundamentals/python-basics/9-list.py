### Access list ####

# my_list = [25,43,23,22,12]

# print(my_list)
# print(my_list[0])
# print(my_list[-1])  # -1 means last index


### List slicing ###

# print(my_list[0:3])
# print(my_list[0:5:2])
# print(my_list[0::2])
# print(my_list[:8:2])
# print(my_list[-4:])
# print(my_list[::-1]) #reverse
# print(my_list[::])   #all
# print(my_list[:])    #all

### List modify ###

# fruits = ['apple', 'banana', 'strawberry']

# fruits[1] = 'blueberry' #change in list
# print(fruits)

# fruits.append("mango") #adding element at the last of the list #method
# print(fruits)

# fruits.remove("strawberry") #remove an element from the list #method
# print(fruits)

#### List methods #####

# more_fruits = ["orange","cherry"]
# fruits.extend(more_fruits)         #extend - as like as .append()
# print(fruits)

# fruits.insert(1, "avocado")  #insert - insert items index wise - do not remove the old item
# print(fruits)

# veg = ['carrot', 'potato', 'tomato', 'potato']
# veg.remove('potato') # remove- (permanently) - if there are duplicate items , it removes first one
# print(veg)

# fruits.clear()         #clear all elements/items
# print(fruits)

# m_string = ['a', 'b','c', 'd', 'b', 's','f','h','b','k','l']

# ind = m_string.index("b")   #finding index number/position - for duplicate items , it shows the first one's index position 
# print(ind)

# indx = m_string.index("b",2)   #finding index starting from 2
# print(indx)

# indx = m_string.index("b",2,6)   #finding index starting from index 2 and ends in index 5
# print(indx)

# print(m_string.count("b")) #count specific element

# m_string.reverse()  #reverse - ((permanently))
# print(m_string)

# num = [10,25,40,8,24,14,10,23]
# num.sort()           #default sort ascending order  (small to large) - ((permanently))
# print(num)

# num.sort(reverse = True) # to sort in descending order (large to small) - ((permanently))
# print(num)

# obj = ['key', 'ball','airpod','cup','dfsfadfdf']

# obj.sort() #default sort in ascending order for alphabetical word(starting a-b-c...)
# print(obj)

# obj.sort(key = len) #default sort in ascending order on the basis of length
# print(obj)

# obj.sort(key = len, reverse=True) #sort in descending order on the basis of length
# print(obj)

# num1= [24,58,69,21,46,787]
# popped = num1.pop(2)  #pop removes/takes the element index-wise and "return" it - (permanently)
# print(popped)
# print(num1)

# num2 = [24,58,69,21,46,787]
# popped = num2.pop()  #by default pop removes/takes the last element and "return" it
# print(popped)
# print(num2)

# obj1= ['egg','oil','salt', 'coconut']
# o_copy = obj1.copy() #to create shallow copy
# print(o_copy)

# o_copy.append('jojoba') # modifying copy doesn't affact the original one 
# print(o_copy)
# print(obj1)


### join list ####

# list1= [1,2,3]
# list2 = ['a','b']

# f_list = list1 + list2  #to join lists using "+" operator
# print(f_list)

# for x in list2:
#     list1.append(x) # to join lists using 'append'
# print(list1)

# list1.extend(list2) #to join lists using 'extend'
# print(list1)


################################ List comprehensions ############################################
### syntax: list_name = [expressions 'for' item 'in' iterable 'if' condition]
### 3 main components in list comprehensions are: 1.expression, 2.for clasue, 3.if condition(optional)

# squares_list = [x**2 for x in range(1,6)] #create list of squares , example- list comprehension
# print(squares_list)

# even_list = [x for x in range(1,11) if x%2 == 0] #create list of even number , another example
# print(even_list)

# n_list = ['saiful','islam','rupom']
# u_list =[x.upper() for x in n_list]  #to make the element in upper case , another example
# print(u_list)

# nst_lst = [[1,2],[3,4],[5,6]]

# flat_lst = [item for sublist in nst_lst for item in sublist] #to flatten single list from sublist - not unterstood
# flatten_lst = [ x for y in nst_lst for x in y] # same as above, just different variable 
# print(flat_lst)
# print(flatten_lst)


### List iteration ### 

# x_lst = ['egg','cook','rice','tiger']
# for x in x_lst:                          #using for loop
#     print(x)


# index = 0
# x2_lst = ['rose','winter','play','baby']
# while index < len(x2_lst):                  #using while loop
#     print(x2_lst[index])
#     index +=1


# print(x2_lst[1])
