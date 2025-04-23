### 1. Limit the decimal places to 2 digits using .format method and print result, for the variable pi = 3.14159265359

# pi = 3.14159265359
# print("Value of pi is: {:.2f}" .format(pi))


### 2. Extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course", slice characters from index 2 to 8, skipping every other char.

# my_string = "Python Course"
# print(my_string[2:8:2])

### 3. Slice to get only the middle character(s): For my_string = "Madhav", use slicing to extract the middle character(s).

# str1 = "Madhav"
# str2 = "Madhava"
# print (len(str1))
# print(len(str2))

# def m_w(word):
#     m = int(len(word)/2)
#     if len(word) % 2 == 0:
#         return word[m-1:m+1]
#     else:
#         return word[m]
# print(m_w(str1))
# print(m_w(str2))

### 4. Remove the first 3 and last 3 characters: Given my_string = "Regression Analysis", remove the first 3 and last 3 characters.

# mstr = "Regression Analysis"
# print(mstr[3:-3])


### 5. Get the substring that starts 4 characters from the end to the last character: For my_string = "Classification", slice the string starting from the 4th character from the end to the last character.

# nstr = "Classification"
# print(nstr[-4:])

### 6. How to Reverse a String Using Python String Methods? 

# word = "Python"
# print(word[::-1])

### 7. Write a Python function to check if a string is a palindrome using string methods.

# pstr = "madam"
# nstr = "common"

# def check_palingdrome(s):
#     if s == s[::-1]:
#         print (f"{s} is a plingdrome")
#     else:
#         print(f"{s} is not a plingdrome") 
# check_palingdrome(pstr)
# check_palingdrome(nstr)