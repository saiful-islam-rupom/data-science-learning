# import re      # re (module) stands for regular expression

# def check_con(text):
#     if len(text) < 8:
#         return "Weak: Password must contain 8 character"
#     if not any(char.isdigit() for char in text):               # not fully clear about {not any()}
#         return "Weak: Password must contain a digit"
#     if not any(char.isupper() for char in text):
#         return "Weak: Password must contain a upper letter"
#     if not any(char.islower() for char in text):
#         return "Weak: Password must contain a lower letter"
#     if not re.search(r'[!@#$%^&*(){}?><.,]', text):            # .search() - function from re
#         return "Medium: Password should contain a special character"
#     return "Strong! Your password in secured."

# def password_checker():
#     print("Welcome to our tool")
#     while True:
#         password = input("Enter your password.(To quit, type 'exit'): ")
#         if password.lower() == 'exit':
#             print("Thank you for using our tool")
#             break
#         result = check_con(password)
#         print(result)

# if __name__ == '__main__':   # to run/execute password_checker function at first
#     password_checker()



### alternative using elif statement - more optimized
# import re      

# def check_con(text):
#     if len(text) < 8:
#         return "Weak: Password must contain 8 character"
#     elif not any(char.isdigit() for char in text):               
#         return "Weak: Password must contain a digit"
#     elif not any(char.isupper() for char in text):
#         return "Weak: Password must contain a upper letter"
#     elif not any(char.islower() for char in text):
#         return "Weak: Password must contain a lower letter"
#     elif not re.search(r'[!@#$%^&*(){}?><.,]', text):            
#         return "Medium: Password should contain a special character"
#     else:
#         return "Strong! Your password in secured."

# def password_checker():
#     print("Welcome to our tool")
#     while True:
#         password = input("Enter your password.(To quit, type 'exit'): ")
#         if password.lower() == 'exit':
#             print("Thank you for using our tool")
#             break
#         result = check_con(password)
#         print(result)

# if __name__ == '__main__':
#     password_checker()