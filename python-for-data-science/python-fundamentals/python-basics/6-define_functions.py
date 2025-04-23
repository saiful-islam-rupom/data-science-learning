# def add2num(a, b):
#     result = a + b
#     print("The sum is:", result)

# add2num(5,2)


# def add3num(a,b,c):
#     return a+b+c

# print(add3num(2,3,4))


# def converter(cel):
#     fah = ((9*cel)/5)+32
#     return fah

# f = converter(25)
# print("Fahrenheit:", f)


#### Making a simple calculator ######
# def sum(a,b):
#     sm = a + b 
#     return sm
# def sub(a,b):
#     sb = a - b
#     return sb
# def mul(a,b):
#     mu = a*b
#     return mu
# def div(a,b):
#     di = a/b
#     return di
# def avg(a,b):
#     av = (a+b) /2
#     return av

# print("Select an operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Average")
# select = int(input("Select operation: "))
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if select == 1:
#     print(a,"+",b,"=",sum(a,b) )
# elif select == 2:
#     print(a,"-",b,"=",sub(a,b) )
# elif select == 3:
#     print(a,"*",b,"=",mul(a,b) )
# elif select == 4:
#     print(a,"/",b,"=",div(a,b) )
# elif select == 5:
#     print("Average of",a,"&",b,"=",avg(a,b) )
# else:
#      print("You entered wrong keyword for operation")


######  argument unpacking operators (or variable-length arguments) ##### - here we can use as many arguments as we want
#######  (*arg) - positional arguments ######## - It collects all arguments into a tuple - (1, 2, 3, 4)

# def add_num(*nums):  
#     return sum(nums)

# print(add_num(1,2,3,4))

# print(add_num(*range(100)))  # 100 arguments (0 to 99)


###### (**arg) - Keyword arguments(key-value pairs) ###### - It collects all arguments into a dictionary - {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

# def add_num(**nums):  
#     return sum(nums.values())   # Summing the dictionary values
 
# print(add_num(x=10, y=20))


