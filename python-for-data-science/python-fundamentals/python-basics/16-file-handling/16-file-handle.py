####### file handling ########
### file handling mode: r-read, w-write, a-append
### structure of file handling - open file -> read/write/append -> close file

### Handling a file ###
### read ###
# file = open(r"E:\Data_Science\learn_python\python_folder\python_basic\16-file_handling\example.txt",'r') # here first 'r' is used to get rid from unexpected (\)-error
# content = file.read()   #to read entire file
# print(content)
# file.close() #best practice

# file = open(r"E:\Data_Science\learn_python\python_folder\python_basic\16-file_handling\example.txt",'r')
# content = file.readline()   # .readline() - to read frist line
# print(content)
# file.close()

# file = open(r"E:\Data_Science\learn_python\python_folder\python_basic\16-file_handling\example.txt",'r')
# content = file.readlines()   # .readlines() - to read entire file - list wise
# print(content)
# file.close()

### write ###
# file = open(r"E:\Data_Science\learn_python\python_folder\python_basic\16-file_handling\example1.txt",'w')
# file.write("Lets go.")
# file.close()

# file1 = open(r"E:\Data_Science\learn_python\python_folder\python_basic\16-file_handling\example1.txt",'a')  # append - a type of write file
# file1.write("\nHurry up!")
# file1.close()


### using 'with' statement -there is no need to use .close()

# with open(r'E:\Data_Science\learn_python\python_folder\python_basic\16-file_handling\example1.txt','r') as file:
#     content = file.read()
#     print(content)