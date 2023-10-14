#Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.

'''
 function can be define with keyword def functionName()

def return_odd():
    x=[]
    for i in range (1,25):
        if i %2 !=0:
            #print("it is odd")
            x.append(i)
    return x

y=return_odd()
print(list(y))


'''

#Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
#to demonstrate their use.
'''
*args:- if we create function with *param then it will accept n number of arguments this is called asterisk( * ) type function
for example


def func(*a)
    print(a)

func(1,2,3,4)
----
for (**args) means it will accept argument with key and value format

for example

def func(**args)
    print(args) 

func(x=0,y=1)    
'''

#Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
#used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
#16, 18, 20].

'''
it is an object which represent the streaming of data and we can loop over data to go in sequence like list , tuple etc
method used for iteration is  for loop, next() , iter() and method used to initialize the iterator object is __iter__()
a=[2, 4, 6, 8, 10, 12, 14,16, 18, 20]
for i in a[0:5]:
    print(i)
'''
#Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
#function.
'''
it is normal function whenever it is need to generate a value it do via yield keyword rather then an return keyword
yield keyword is used to give response one by one instead to give conclude response as return keyword do.

def genfunction()
    yield1:
    yield2
    yield3:

for i in genfunction():
   print(i)    
'''
#Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
#first 20 prime numbers.
'''
def prime_fun(a):
    flag=""
    if a==1:
        #print(a,"it is not prime number")
        return False

    elif a==2:
        #print(a,"it is prime number")
        return True
    else:
      for i in range(2,a):
        if a%i==0:
            #print(a,"it is not prime number")
            flag="Not"
            return False

      if flag !="Not":
        return True

def check_prime(limit):
    count = 2
    while count < limit:
        if prime_fun(count):
            yield count
            count += 1
        else:
            count += 1
#here setting1000 limit to get prime number of upto range of 1000
value = check_prime(1000)
#print(list(value))

for _ in range(20):
    prime = next(value)
    print(prime)
'''

#Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.
'''

def x(limit):
    a,b=0,1
    while a <=limit:
        yield a
        a,b=b,a+b


value=x(50)
print(list(value))
'''
#Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
#Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
'''
value= 'pwskills'
list = [char for char in value]
print(list)
'''

#Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

def is_pali(number) :
    orginal = str(number)
    reve_str = ""

    i = len(orginal) - 1
    while i >= 0 :
        reve_str += orginal[i]
        i -= 1

    return orginal == reve_str


if is_pali(1412) :
    print("The  is a palindrome!")
else :
    print("The  is not a palindrome!")
#Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
'''

number=[x for x in range(1,100)]
list=[x for x in number if x%2!=0 ]
print(list)
'''
