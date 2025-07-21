# # Question 1: Write a Program to find the greatest of four numbers entered by the user.
# number1=int(input("Enter your 1st number here :"))
# number2=int(input("Enter your 2nd number here :"))
# number3=int(input("Enter your 3rd number here :"))
# number4=int(input("Enter your 4th number here :"))
# if(number1>number2 and number1>number3 and number1>number4):
#     print(f"{number1} is greater than {number2,number3,number4}!")
# elif(number2>number1 and number2>number3 and number2>number4):
#     print(f"{number2} is greater than {number1,number3,number4}!")
# elif(number3>number1 and number3>number2 and number3>number4):
#     print(f"{number3} is greater than {number1,number2,number4}!")
# elif(number4>number1 and number4>number3 and number4>number2):
#     print(f"{number4} is greater than {number1,number2,number3}!")
# else:
#     print("Wrong Chosse..!")






# # Question 2: write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.Assume 3 subjects and take marks as an input from the user .
# marks1=int(input("Enter your marks1 here :"))
# marks2=int(input("Enter your marks2 here :"))
# marks3=int(input("Enter your marks3 here :"))

# total_percentage=(100)*((marks1+marks2+marks3)/300)

# if( total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
#     print(f"You are promoted in next class with {total_percentage} %")
# else:
#     print("Better luck next time..!")





# # Question 3: A spam comment is defined as a text containing following keywords : "Make a lot of money","buy now","subscribe this","click this".Write a program to detect these spams.
# senetence=["make a lot of money","buy now","subscribe this","click this"]
# message=input("Enter your message here :")
# if message in senetence:
#     print("Spam")
# else:
#     print("Not Spam")






# # Question 4: Write a program to find whether a given username contains less than 10 characters or not.
# username=input("Enter your username here:")
# if(len(username)<=10):
#     print("Username under 10 characters")
# else:
#     print("Username is greater than 10 characters!")



# #Question 5: Write a program which finds out whether a given name is present in a list or not.
# names_list=["Umang","Kunal","Tanuj","Komal","Yash","Khushi","Prajwal","Santosh"]
# your_name=input("Enter your name here :")
# if (your_name in names_list):
#     print("Congratulation 🎉,You are in list.")
# else:
#     print("Better luck next time 😒!")