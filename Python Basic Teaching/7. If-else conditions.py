from random import *

light = ["red", "yellow", "green"]
a = choice(light)
print("Current Light in the street lamp: ",a.title())

if(a == "green"):
    print("Go!")

elif(a == "red"):
    print("Stop!")

elif(a == "yellow"):
    print("Slow Down!")

else:
    print("Undefined! Sorry!")