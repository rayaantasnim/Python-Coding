a = 100
b = 232
c = 73
d = 10

#How to addition two numbers?
print(a+b)

#Low efficient:
add = a + b
print("The final result after the addition is:", add)

#Advanced way:
if(a and b):
    print("Added result", a+b)
    print("Substracted result", a-b) #subtract
print("")

#Multiply
print(f"After the multiply, the result is: {a*b*c*d}")

#Divide
print(f"Divide the number: {a/d}")
print(f"Float as a result: {b/a}")
print(f"Conversion of float: {b//a}")

#Low efficient way to convert the float
div = b/a
div = int(div)
print(div)
print("\n\n")

#Square or power
print(a **2)
print(c**12)
print("")

#Square root?
number= 10000
number2 = 121 

import math
result = math.sqrt(number)
print(result)

#Advanced way
from math import *
print(sqrt(number2))


#Final Summery
if( a and b and c and d and number):
    print("Addition result:", a+b+c+d)
    print("Substract result:", a-b-c-d)
    print("Multiply result:", a*b*c*d)
    print("Division result:", b/a)
    print("Division result as integer:", b//a)
    print("Power applying:", a**3)
    print("Square root of", number, "is:", sqrt(number))


