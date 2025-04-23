### handling general type of error ###

# a = input("Enter any number: ")
# b = input("Enter the percentage(%): ")


## example1
# try:        # this is called exception handling - means the program will not stop and give specified output if user enter any invalid input.
#     c = print(f"The percentage of the choosen number is: {(int(a)*int(b))/100}")
# except Exception as e:
#     print(e)

## example2
# try:
#     c = print(f"The percentage of the choosen number is: {(int(a)*int(b))/100}")
# except Exception as e:
#     print("You entered invalid input")

# print("Thanks for using our tool")



### handling specific type of error ###

# print("Here the given list is: [6,3]")
# a = [6,3]
# try:
#     num  = int(input("Enter a index number(integer) for the list: "))
#     print(a[num])
# except ValueError:
#     print("You entered wrong input(type)!!!")
# except IndexError:
#     print("You entered wrong index number that don't exist!!!")
# else:
#     print("Thank you :) You entered inputs correctly :)")

