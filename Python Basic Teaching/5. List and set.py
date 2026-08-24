#new deta set -> List -> Horizontal deta structure

list = [100, 68, 34, 987, 56.765, 345, 00, "Rayaan", "Earth", "Jupiter", "d53657", 00, 343]
print("Previous list:",list)
print("Zero in the list:", list.count(0), "times exist")

if not 167 in list:
    list.append(167) #-> add in the last

list.insert(3, 879)
list.pop(7) 

if 345 in list:
    list.remove(345)
print("Updated list:",list)

#List slicing
string = []
integer = []
for i in list:
    t = str(type(i))

    if ('str' in t):
        string.append(i)

    elif('int' in t):
        integer.append(i)

print(f"\n\nSliced alphabetical list:{string} \nSliced numeral list: {integer}")

#Arithmatic tasks
print(f"Maximum value: {max(integer)} \nMinimum value: {min(integer)}")
#List indexing
