# # Task: 8
# # Create a calculator that can: Add , Subtrac , Multilpy , Divide


# # take input from user..
# num_1 = float(input("Enter first number :"))
# num_2 = float(input("Enter last number :"))

# print("Chose operator")
# print("1. Add")
# print("2. Subtrac")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter you choice(number/character) :")

# if choice == "1" or choice == "Add":
#     print("Result :", num_1 + num_2)

# elif choice == "2" or choice == "Subtrac":
#     print("Result :", num_1 - num_2)

# elif choice == "3" or choice == "Multiply":
#     print("Result :", num_1 * num_2)

# elif choice == '4' or choice == "Divide" :
#     if num_2 == 0 :
#         print("You can't divide number by zero !")
#     else :
#         print("Result :", round(num_1 / num_2 , 2))

# else :
#     print("Invalid choice !")



# # Task: 9
# #  Take user score and  Find Student Grade.


# Score = float(input("Enter the Score :"))

# if Score >= 90 and Score <= 100 :
#     grade = "A+"
# elif Score >= 80 and Score <= 89 :
#     grade = "A"
# elif Score >= 70 and Score <= 79 :
#     grade = "A-"
# elif Score >= 60 and Score <= 69 :
#     grade = "B"
# elif Score >= 50 and Score <= 59 :
#     grade = "C"
# elif Score >= 40 and Score <= 49 :
#     grade = "D"
# elif Score < 40 and Score > 0 :
#     grade = "F"

# else:
#     grade = "Invalid score !"


# print("The student's grade are :",grade)



# # Task: 10 
# # Write a program that checks: Positive, Negative and Zero number.


# num = int(input("Enter the number you want :"))

# if num > 0 :
#     print("Your entered number is positive :",num)
# elif num == 0 :
#     print("Your entered number is Zero :",num)
# else :
#     print("Your entered number is Negative:",num)



# # Task: 11

# # A shop gives discount based on total bill:

# # Bill ≥ 5000 → 20% discount
# # Bill ≥ 3000 → 10% discount
# # Bill ≥ 1000 → 5% discount
# # Otherwise → No discount
# # 👉 Task:
# # Take bill amount from user and print final payable amount.


# bill = float(input("Enter the bill :"))

# if bill >= 5000 :
#     Discount = round(bill * 0.2 , 2)
# elif bill >= 3000 :
#     Discount = round(bill * 0.1 , 2)
# elif bill >= 1000 :
#     Discount = round(bill * 0.05 , 2)
# else :
#     Discount = 0
 

# final_payment = bill - Discount

# print(f"You are getting {Discount}tk discount. ")
# print("Your have to pay :",final_payment)



# # Task:12

# # 🚦 2. Traffic Light System
# # Input color from user:

# # "red" → Stop
# # "yellow" → Ready
# # "green" → Go

# # 👉 Task: Print the correct action.


# color = input("Enter the color(red/yellow/green):")

# if color.lower() == "red":
#     action = 'Stop'

# elif color.lower() == 'yellow' :
#     action = 'Ready'

# elif color.lower() == 'green' :
#     action = 'Go'

# else :
#     action = 'Invalid color !'

# print("Now you can ",action)



# # Task:13

# # 📱  Mobile Data Usage Alert
# # User enters used data (GB):

# # ≥ 10 GB → Heavy User
# # ≥ 5 GB → Normal User
# # < 5 GB → Light User

# # 👉 Task: Print user type.


# data = float(input("Enter how many GB you have used :"))

# if data >= 10 :
#     user_type = 'Heavy user'
# elif data >= 5 :
#     user_type = 'Normal user'
# else :
#     user_type = 'Light user'

# print(f'you are a {user_type} you have used {data}GB')



# # Task: 14

# # 🎓 4. Student Attendance System
# # Take attendance percentage:

# # ≥ 75 → Allowed in exam
# # < 75 → Not allowed

# # 👉 Task: Print result.


# attendance = int(input("Enter your attendance parcentange :"))

# if attendance >= 75 and attendance < 100 :
#     result = "Allowed in exam"
# elif attendance < 75 and attendance > 0 :
#     result = "Not allowed" 
# else :
#     result = "Invalid attendance"

# print(f"you are {result} because your attendance is {attendance}%")