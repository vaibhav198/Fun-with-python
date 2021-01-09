"""
Swapping two numbers in python is really cool.
In C/C++, we need to take one extra (temp) variable (without pointer)
""" 
#Swapping two numbers
x = 10
y = 11
print("x = {} and y = {}".format(x, y)) #x = 10 and y = 11
y,x = x,y
print("x = {} and y = {}".format(x, y)) #x = 11 and y = 10
#swapping more than two variable
a = 10
b = 20 
c = 30
print ("a = {}, b = {}, and c = {}".format(a, b, c)) #a = 10, b = 20, and c = 30
c,b,a = a,b,c
print ("a = {}, b = {}, and c = {}".format(a, b, c)) #a = 30, b = 20, and c = 10
