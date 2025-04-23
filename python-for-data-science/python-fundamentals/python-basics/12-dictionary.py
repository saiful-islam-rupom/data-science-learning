### create dictionary ###

# my_dic = {"Name":"Saiful", "Age": 24, "Gender":"Male", "Email": "fgfgf@gmail.com"}
# print(my_dic)

# n_dic = {} #empty dic
# print(n_dic)

# person = dict(name="Saiful", age =24, gender= "Male") #using constructor
# print(person)

# std = dict([("name","Saiful")  , ("age", 24) ,  ("gender","Male")]) #usind constructor with list of tuples
# print(std)


### access dictionary ####

# print(person["name"])  
# print(person["age"])
# print(person["profession"])  #if not found it shows error


#### dictionary methods ####

# print(my_dic.keys())   #return all keys

# print(my_dic.values())   #return all values

# print(my_dic.items())   #return all key-value pair      # item = key-value pair

# print(my_dic.get("Email"))   #return the value of specified key
# print(my_dic.get("Age"))
# print(my_dic.get("Class"))  #if not found it doesn't return error
# print(my_dic.get("Profession", "Engineer"))     #we can assign new item if there is no item such that
# print(my_dic)


###  Add/modify items in dictionary ###

# student = {
#     "name" : "Sumon",
#     "roll no" : 22,
#     "age" : 10,
#     "level" : "Primary"
# }

# student['DOB'] = 2012        #add item - (permanent)
# print(student)

# student["roll no"] = 21 #modify/replace item  - (permanent)
# print(student)

# del student['age']  #delete/remove item - (permanent)
# print(student)

# trash = student.pop('level') #remove the item from dictionary and ruturn it - (permanent)
# print(trash)
# print(student)


###### dictionary iteration ######
### using for loop ###

# for key in student:   #loop through keys (direct iteration is for keys)
#     print(key)
# for key in student.keys(): # alternative
#     print(key)

# for key_name in student:   #loop through value
#     print(student[key_name])
# for value in student.values(): # alternative
#     print(value)


# for item in student.items(): #loop through item(key, value)
#     print(item)
# for key,value in student.items(): # alternative - but unorganized
#     print(key, value)


#### nested dictionary #####
# main_student = {
#     "student1" : {"name" : "Asif" ,"age" : 20},
#     "student2" : {"name" : "Sajan", "age" : 19, "grade" : "A+"}
# }
# print(main_student)


###### access values ######

# print(main_student['student1'])
# print(main_student['student2']['name'])


###### dictionary comprehensions #####
### syntax: n_dic = {key_expression: value_expression 'for' item 'in' iterable 'if' condition}

# squares = {x: x*x for x in range(1, 6)}
# print(squares)

