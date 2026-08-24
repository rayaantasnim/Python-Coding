from random import *

a = random()
print(a)

a = ["Red","Green","Blue"]
print(choice(a))

list = []
for i in range(101):
    list.append(i)

print(list)
print("")

for element in list:
    print(element)

print("\n\nChoosen randomly:",choice(list))