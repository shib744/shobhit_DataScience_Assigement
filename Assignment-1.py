#Question1


multi_type=["shobhit",[1,2,4],7.5,(1,2)]

for i in multi_type:
    print(type(i))

#Question 2
#var1 = ‘ ‘ --> string
#var2 = ‘[ DS , ML , Python]’  --> string
#var3 = [ ‘DS’ , ’ML’ , ‘Python’ ] --- > list
#var4 = 1. --> float

#Q3. Explain the use of the following operators using an example:
'''
(i) / --> arithmetic operator for division
(ii) % --> arithmetic operator used for modulus division
(iii) // -- >  floor division 
(iv) ** --> ex- a**b means a is to power b
'''

#question4

list=["yahoo",5.6,7,[2,3,4],7,9,6,0,"shobhit",(7,6)]

for i in list:
    print(i,type(i))

#question5
a = 13
b = 4
i = 0
while a >= b :
    if (a % b) == 0 :
        print("it is divisible")
        i+=1
    b+=1
print("number of times it is divisible",str(i))

#question5
for i in range(1,25):
     if (i%3)==0:
         print(i,"it is divisible")
     else:
         print(i,"it is not divisible")


#Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property.
#Ans:-mutable means where value can be changed while non mutable value can not eb changed
#for example

#mutable example

i="shobhit"

for x in i:
    x[3]='L'

#non mutable
list=[1,2,3]
list[0]=7
print(list) 
