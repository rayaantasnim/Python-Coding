#For loop
#1 Argument given as a parameter
for i in range(100):
    print(f"{i}. This is a python - for loop.")

print("\n\n\n")


#2 Argument given as parameter
for i in range(20, 100):
    print(f"{i}. This is an updated for loop. Started from 20.")

print("\n\n\n")

#3 (highest) Argument given as parameter
for i in range(20, 100, 5):
    print(f"{i}. This is an updated for loop. Started from 20. And it is special one.")


print("\n\n\n")
#Task - muliply table creat 
a = 5
list = []
for i in range(11):
    print(f"{a} multiply with {i}, answer is {a*i}")
    list.append(a*i)


user = []
for i in range(100):
    value = input("Enter a numerical velue here or say 'Break' to stop:  ")
    if not value == "break":
        user.append(int(value))
        continue

    elif value == "break":
        if(user):
            print("Here is your list:", user)
        break 

#While loop 
i = 0
while(True):
    i +=1 #-> i = i + 1
    print(i, ". I am Rayaan Tasnim.")
    if(i>10):
        break

    else:
        continue