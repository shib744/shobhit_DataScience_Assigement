#Q1. How do you comment code in Python? What are the different types of comments?
#we can add comment in python via starting with "#" keyword or starting and ending with '''
#and we have three ways to add comment in python 1) single  2) multi-line and 3) docstrings which we can  define after
#any function , module or method


#Q2. What are variables in Python? How do you declare and assign values to variables?
'''
variable reserved memory location to store value in python , every variable have data type

we can declare variable like a="shobhit" or myvar=44.44  in python
'''

#Q3How do you convert one data type to another in Python?
'''
you can convert one datatype to another by type casting , for example convert integer to string like below 
a= 4 
b=str(a) so now b is having 4 but type as string
'''

#Q4. How do you write and execute a Python script from the command line?

'''
you need to first setup python on you local machine and verify python version by typing "python" on cmd after
that create one file with extension .py and write logic in that file and then call that file from cmd like
python myfile.py , it will give output of that file
'''

#Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
'''
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])
'''
#Q6. What is a complex number in mathematics, and how is it represented in Python?
'''
complex number are expressed in math  by x+yj sum of real number and imaginary number , here x and y are real number and j is imaginary
'''

#Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
# age=25

#Q8.Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
'''
price=9.99 
it is having data type float , print(type(price))
'''

#Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?
'''
name="shobhit"
print(name)
'''

#Q10. Given the string "Hello, World!", extract the substring "World".
a="Hello, World!"
print(a[7:12])

#Q11.Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.
user="student"
if user == "student":
    is_student=True
else:
    is_student = False
print(is_student)