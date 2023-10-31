#Q1. Create a python program to sort the given list of tuples based on integer value using a
#lambda function.
'''
my_tuple=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

result=lambda x:x[1]


my_tuple.sort(key=result)
print(my_tuple)
'''
'''
Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

value=map(lambda x:x**2,y)

print(list(value))

'''

#Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
#lambda functions
'''
y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value=tuple(map(lambda x:str(x),y))

print(value)
'''

#Q4. Write a python program using reduce function to compute the product of a list containing numbers
#from 1 to 25.
'''
from functools import reduce

number=list(range(1, 26))

result=reduce(lambda x,y:x*y,number)
print(result)
'''

#Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
#filter function.
'''
number=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

result=list(filter(lambda x: x%2==0 and x%3==0, number))
print(result)
'''
#Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
#function.
'''
my_list=['python', 'php', 'aba', 'radar', 'level']

result=list(filter(lambda x:x[::-1]==x,my_list))
print(result)
'''
