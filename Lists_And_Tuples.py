# Question 1: Write an python program to store seven fruits in a list entered by the user.
fruits=[]
f1=input("Enter fruit name:")
fruits.append(f1)

f2=input("Enter fruit name:")
fruits.append(f2)

f3=input("Enter fruit name:")
fruits.append(f3)

f4=input("Enter fruit name:")
fruits.append(f4)

f5=input("Enter fruit name:")
fruits.append(f5)

f6=input("Enter fruit name:")
fruits.append(f6)

f7=input("Enter fruit name:")
fruits.append(f7)
print(fruits)

                               #or

fruits=[]
for i in range(1,8):
    name=input("Enter Fruits name :")
    fruits.append(name)
print(fruits)

# Question 2: Write a python program to accept marks of 6 students and display them in sorted manner.
marks=[]
for i in range(1,7):
    num=int(input("Enter your marks:"))
    marks.append(num)
print("Marks without Sorted :",marks)
marks.sort()
print("Marks with sorted:",marks)



# Question 3: Check that a tuple type cannot be changed in python.
tup=(1,2,"Umang")
tup[3]="Sharma"
print(tup)




# Question 4: Write a program to sum a list with 4 numbers.
list=[1,2,3,4]
print(sum(list))




#Question 5: Write a program to count the numbers od zeros in the following tuple: a=(7,0,8,0,0,9).
a=(7,0,8,0,0,9)
n=a.count(0)
print(n)