# Question 1: Write a program to create a dictionary of Hindi words with values as their English transaction.Provide user with an option to look it up!
Hindi_Words={
    "kaha":"Where",
    "kya":"What",
    "kyo":"Why"
}
words=input("Enter your Hindi Word here :")
print(Hindi_Words[words])





# Question 2: Write a program to input eight numbers from the user and display all the unique numbers(once).
s=set()
for i in range(1,9):
    numbers=int(input("Enter Your number here: "))
    s.add(numbers)
print(s)







# Question 3: Can we have a set with 18(int) and '18'(str) as a value in it?
set={18,'18'}
print(set)
#output= Yes, We can.






# Question 4: What will be the length of following set s:  s=set()      s.add(20)       s.add(20.0)     s.add('20).
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
# Output= 3.






# Question 5: Create an empty dictionary . Allow 4 friends to enter their favourite language as value and use keys as their names. Assume that the names are unique.
dict={}
for i in range(1,5):
    name=input("Enter your name here :")
    language= input("Enter your language here :")
    dict.update({name:language})
print(dict)









