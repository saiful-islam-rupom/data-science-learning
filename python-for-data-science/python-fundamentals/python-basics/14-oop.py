#### using oops to create student records ####

# class Student:       # class - blueprint or template or mold --- as like as dictionary
#     def __init__(self, name, grade, percentage):  #method
#         self.name = name     #attribute
#         self.grade = grade   #attribute
#         self.percentage = percentage #attribute
#     def student_details(self): #method
#         print(f"{self.name} is in class {self.grade} with {self.percentage}%" )

# student1  = Student('Madhav', 11, 99)  # object - instance or product of a class
# student2  = Student('Rishhav', 12, 95)

# print(student1.name, student1.grade)

# student1.student_details()

# student2.student_details()

# print(student1.__dict__)


#### modify object property/attribute #####
# student1.percentage = 100
# print(student1.percentage)
# print(student1.__dict__)

### delet object property ###
# del student1.grade
# print(student1.__dict__)

### delet object ###
# del student1
# print(student1.__dict__) # error - because student1 is deleted


###### 4 basic things in oop ####
### 1.Abstraction ### - hiding unnecessary details from user
# class Student:
#     def __init__(self, name, grade, percentage,team):  
#         self.name = name     
#         self.grade = grade   
#         self.percentage = percentage   
#         self.team = team
#     def student_details(self):
#         print(f"{self.name} is in class {self.grade} with {self.percentage+1}% in team {self.team}" ) # here- +1 is added as an Abstraction
# team1 = 'A'
# team2 = 'B'
# student1  = Student('Madhav', 11, 99, team1)
# student2  = Student('Rishhav', 12, 95, team2)

# student1.student_details()
# print(student1.__dict__)


### 2.Encapsulation ### - to private methods and attributes
# class Student:
#     def __init__(self, name, grade, percentage,team):  
#         self.name = name    
#         self.grade = grade  
#         self.__percentage = percentage   #here __ is used to encapsulate
#         self.team = team

#     def get_percentage(self):       #to access encasulated attributes   
#         return self.__percentage
#     def student_details_sus(self):  #sus - for student users
#         print(f"{self.name} is in class {self.grade} with {self.get_percentage()}% in team {self.team}" ) 
#     def student_details_ad(self):   #ad - for administration
#         print(f"{self.name} is in class {self.grade} with {self.__percentage}% in team {self.team}" )
#     def student_details_nus(self):   #nus - for normal users
#         print(f"{self.name} is in class {self.grade} with {self.percentage}% in team {self.team}" )
# team1 = 'A'
# team2 = 'B'
# student1  = Student('Madhav', 11, 99, team1)
# student2  = Student('Rishhav', 12, 95, team2)

# student2.student_details_sus()  

# print(student2.get_percentage())

# student2.student_details_ad() 

# student2.student_details_nus() # error- because there are no 'self.percentage' attribute


### 3.Inheretance ###

# class EU_Student:  #parent-class
#     def __init__(self, name, id, department, cgpa):  
#         self.name = name      
#         self.id = id    
#         self.department = department
#         self.cgpa = cgpa
#     def eu_student_details(self):
#         print(f"Student ID is: {self.id}.\nHis/her name is: {self.name}.\nHe/she is in {self.department} department.\nHis/her current CGPA is: {self.cgpa}" )
# student1  = EU_Student('Saiful', 201400077 , 'CSE', 3.37)
# student2  = EU_Student('Robin', 220600018, 'BBA', 3.17 )
# # student1.eu_student_details()

 
# class Graduate_Student(EU_Student):  #child-class
#     def __init__(self, name,id, alumni_id, department, cgpa):
#         super().__init__(name, id, department, cgpa)  #calling parent-class init  -   using inheretance
#         self.alumni_id = alumni_id
#     def g_student_old_details(self): 
#         print(super().eu_student_details())  #calling parent-class method -  using inheretance
#     def g_student_current_details(self):
#         print(f"Alumni ID is: {self.alumni_id}.\nHis/her name is: {self.name}.\nHe/she is in {self.department}.\nHis/her final CGPA is : {self.cgpa}")
# graduate_student1 = Graduate_Student('Rakibul',201400084,84,'CSE', 3.09 )
# graduate_student2 = Graduate_Student('Saiful',201400077,77,'CSE', 3.37 )

# print(graduate_student1.cgpa)

# graduate_student1.g_student_old_details()

# graduate_student2.g_student_current_details()

# graduate_student2.g_student_old_details()

# print(graduate_student2.alumni_id)



### 4. Polymorphism ### - both/multiple classes have same method name, but output of the methods will be different according to the object's class

# class EU_Student:   
#     def __init__(self, name, id, department, cgpa):  
#         self.name = name      
#         self.id = id    
#         self.department = department
#         self.cgpa = cgpa
#     def student_details(self):  # polymorphism - both classes has same method name- 'student_details()'
#         print(f"Student ID is: {self.id}.\nHis/her name is: {self.name}.\nHe/she is in {self.department} department.\nHis/her current CGPA is: {self.cgpa}" )
# student1  = EU_Student('Saiful', 201400077 , 'CSE', 3.37)
# student2  = EU_Student('Robin', 220600018, 'BBA', 3.17 )

# class Graduate_Student(EU_Student): 
#     def __init__(self, name,id, alumni_id, department, cgpa):
#         super().__init__(name, id, department, cgpa)   
#         self.alumni_id = alumni_id
#     def student_details(self):  # polymorphism - both classes has same method name- 'student_details()'
#         print(f"Alumni ID is: {self.alumni_id}.\nHis/her name is: {self.name}.\nHe/she is in {self.department}.\nHis/her final CGPA is : {self.cgpa}")
# graduate_student1 = Graduate_Student('Rakibul',201400084,84,'CSE', 3.09 )
# graduate_student2 = Graduate_Student('Saiful',201400077,77,'CSE', 3.37 )

# student1.student_details() # polymorphism occured here
# print()
# graduate_student2.student_details() # polymorphism occured here


