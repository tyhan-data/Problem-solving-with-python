# # Task: 1 
# # Take two numbers from user, print: Sum , Difference , Multiplication , Division


# a = int(input("Enter the first number :"))
# b = int(input("Enter the last number :"))

# sum = a + b
# Differance = a - b
# Multiplication = a * b
# Division = round(a / b , 2)

# print("The summation of two value is :",sum)
# print("The Subtraction of two value is :",Differance)
# print("The multiplication of two value is :",Multiplication)
# print("The divition of two value is :",Division)


#  # Task: 2
#  # Check whether a number is even or odd.


# num = int(input("Enter the number :"))

# if num % 2 == 0 :
#     print(num, 'is even')
# else :
#     print(num, 'is odd')

# # one line solution..    
# print(num, 'is even' ) if num % 2 == 0 else  print(num,'is odd')


# # Task: 3
# # Find the sum of all elements in a list


# list = [43,53,34,64,34,53,73,77]

# total = 0
# for i in list :
#     total+= i

# print("The Sum of the list is :",total)

# # one line solution...
# print("The sum of the list is :",sum(i for i in list))


# # Task: 4
# # Count how many vowels are in a given string.


# text = "Hello! i'm Mosairul Alam Tyhan. I am a future data scientist"
# vowel = 'aeiou'
# vowel_list = []

# for i in text :
#     if i.lower() in vowel :
#       vowel_list.append(i)

# print("The total vowel character is :",len(vowel_list)) 

# # one line solution....
# print("The total vowel character is :",sum(1 for i in text if i.lower() in vowel))


# # Task: 5
# # Reverse a given string.


# name = "Tyhan hasan"

# print("After reversed the string",list(reversed(name)))    # using reversed method
# print("After reversed the string :",name[::-1])            # doing manually


# # Task: 6
# # Find the factorial of a number.


# num = int(input("Enter the number you want :"))
# fact = 1

# for x in range(1, num+1):
#     fact*= x

# print(f"The factorial of {num} is : {fact}")

# # using math library...
# import math
# print(f"The factorial of {num} is : ", math.factorial(num))


# # Task: 7
# # Check whether a number is prime or not.


# import math

# def isprime(num):
#     if num <= 1:
#         return "plese! try again"
    
#     for i in range(2,int(math.sqrt(num))+1):
#         if num % i == 0 :
#             return f"Your entered number is not prime {num}"
    
#     return f"Your entered number is prime {num}"

## take input form user..
# num = int(input("Enter a number :"))
# print(isprime(num))


