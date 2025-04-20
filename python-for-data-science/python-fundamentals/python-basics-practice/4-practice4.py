### 1. Print the while loop output in the same line

# print("Hello", "Welcome", sep = "*", end = " ")
# print("Saiful")
# print("Rupom")

# i = 1
# while i < 4:
#     print(f"Saiful{i}","Islam", sep = "+", end = " " )
#     i += 1


### 2. star pattern (straight triangle)
# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end = "")
#     print()

## alternative
# n = 5
# for i in range(1, n+1):
#         print("*" * i)

### 3. star pattern - inverted triangle
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print("*", end = "")
#     print()
 
## altenative
# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)

### 4. Pyramid pattern
# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i), end = "")
#     print("*" * (2*i -1))

### 5. factorial of a number
# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result
# print(factorial(5))

### 6. Find number of vowels in a sentence
# r ="SaifulIslam"
# v = "AEIOUaeiou"
# def vow(n):
#     result = 0
#     for i in n:
#         if i in v:
#             result += 1
#     return result
# print(vow(r))

### 7. Find the Longest word in a string
# sentence = "Apple is good for health"
# words = sentence.split()  # .split() - split words by the white spaces and put in a list
# print(words) # to understand

# Longest_word = ""

# for word in words:
#     if len(word) > len(Longest_word):
#         Longest_word = word 
# print(Longest_word)

### 8. Do-while_loop in python
# while True:
#     num = int(input("enter a number greater than 10: "))
#     if num > 10:
#         print("you entered valid number")
#         break #break is used to exit the loop if the condition is satisfied
#     else:
#         print("you entered invaild number")

### 9. Fibonacci series
# def fibonacci(n):
#     a,b = 0,1
#     count = 0
#     while count < n:
#         print(a,end=" ")
#         a,b = b,a+b
#         count += 1
# fibonacci(3)