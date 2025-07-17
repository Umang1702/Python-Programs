# Question 1: Write a python program to display a user entered name followed by Good Afternoon using input() function.
name=input("Enter your name :")
print(f"Good Afternoon {name}!")


# Question 2: Write a program to fill in a letter template given below with name and date.
name=input("Enter your name :")
date='17 Feb 2024'
letter=f'''
Dear {name},
You are selected!
{date}'''
print(letter)



# Question 3: Write a program to detect double space in a string.
string="Hello My name is  Umang Sharma "
print(string.find("  "))







# Question 4: Replace the double space from problem 3 with single spaces.
string="Hello My name is  Umang Sharma "
print(string.replace("  "," "))







''' Question 5: Write a following program to format the following letter using escape sequence characters:
letter="Dear Umang, this python program repository is nice.Thanks!"'''
letter="Dear Umang,\n\t this python program repository is nice.\n\tThanks!"
print(letter)

