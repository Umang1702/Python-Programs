# Question 1: Write a Program to find the greatest of four numbers entered by the user.
number1=int(input("Enter your 1st number here :"))
number2=int(input("Enter your 2nd number here :"))
number3=int(input("Enter your 3rd number here :"))
number4=int(input("Enter your 4th number here :"))
if(number1>number2 and number1>number3 and number1>number4):
    print(f"{number1} is greater than {number2,number3,number4}!")
elif(number2>number1 and number2>number3 and number2>number4):
    print(f"{number2} is greater than {number1,number3,number4}!")
elif(number3>number1 and number3>number2 and number3>number4):
    print(f"{number3} is greater than {number1,number2,number4}!")
elif(number4>number1 and number4>number3 and number4>number2):
    print(f"{number4} is greater than {number1,number2,number3}!")
else:
    print("Wrong Chosse..!")



#