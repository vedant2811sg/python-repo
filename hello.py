#this  is a comment line
name="vedant"
print(isinstance(name,str))#true
age =2
print(isinstance(age,float))#false it is int
aged=float(age)
print(isinstance(aged,float))#true
ages=int("20")#this is casting
print(isinstance(ages,int))#true
number="test"
age=int(number)#this will give error because string cannot be converted to int
print(4**2)#this is exponentiation operator
print(5//2)#floor division operator round down the value to nearest integer
print(0 or 1)# 1 is printed prints first value if not false else 2nd value
print(0 and 1)# 0 is printed 
print("hi"or False)#hi is printed because first value is not false
print(False or "hi")#hi is printed because first value is false so it prints second value
print (""" vedant 
       is 
       a good boy""")#multiline printing
#empty string and 0 and Flase are the only false
#any returns true if it is not empty string or 0 or False
a=True
b=False
c=any([a,b])#any returns true if any of the value is true
d=all([a,b])#all returns true if all the values are true
num=complex(2,3)#complex number