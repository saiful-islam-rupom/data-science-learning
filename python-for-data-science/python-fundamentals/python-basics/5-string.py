# name = "Saiful"
# age = 24

# print("My name is %s and I'm %d." % (name, age)) # another writing format

# print("My name is {} and I'm {}." .format(name, age)) # another writing format
# print("My name is {0} and I'm {1}." .format(name, age))
# print("My name is {1} and I'm {0}." .format(name, age))
# print("My name is {name} and I'm {age}." .format(name = "charli", age = 16))

# print(f"My name is {name} and I'm {age}.") # easiest writing format
# print(f"After 5 years I'll be {age + 5}.")

# print("Hello World")
# print("Hello\nWorld")
# print("Hello\tWorld") # 4-space

# a = "hi"
# b = "python"
# print(a+b)
# print(a*3)

# if "h" in a:
#     print("Yes")
# else:
#     print("no")

# print(r"Hello\nworld") # r - is used to write plain text including - \n

##### string indexing ########

# name = "Saiful"

# print (name[0])
# print (name[1])
# print (name[-1])  # -1 means last index / starting from reverse

######### string slicing [start:end:step] ##########

# my_name = "Rupom"

# print(my_name[0:3])
# print(my_name[0:3:1])
# print(my_name[0:-2])

# print(my_name[0:4:2])
# print(my_name[0::2])
# print(my_name[1::2])
# print(my_name[:])
# print(my_name[::])

# print(my_name[::-1]) #all reverse

###### string methods ##########
# word = "Hello, Saiful"

# print(len(word))           #length

# print(word.upper())          #to convert into upper case

# print(word.lower())          #to convert into  lower case

# print(word.count("l"))       #to count specific letter

# print(word.find("e"))  #to find the index position of a given string
# print(word.find("l"))  

# print(word.split("l"))  #to split - using the given string
# print(word.split(","))  

# print(word.replace("Saiful", "Mohin"))  #to replace - syntax: .replace("old_value", "new_value")
# print(word.replace("l", "k"))

# word2 = "Hello, Saiful is great!"
# print(word2.title())          #to make first letter of each word in capital

# word3 = "   I    am good    "
# print(word3.strip())  #to remove white spaces from the firsrt and last of a sentence

# word4 = "Hihohm"
# print("_".join(word4))      #use a type of seperator to join between each string

# word5 = "I", "am", "Rupom"
# word6 = "I am Rupom"
# print(" ".join(word5))
# print(" ".join(word6))