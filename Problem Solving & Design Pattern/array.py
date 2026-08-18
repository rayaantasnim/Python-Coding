# list == array in Python
name = ["Rayaan", "Rafsan", "Afnan", "Ahnaf"]
numbers = [100, 200, 700, 400, 422, 911, 647, 999]

# index starts from zero (0)
# last index = length - 1

numbers.append(1000) #-> add at the last
numbers.insert(0,23) #-> add in the definite position
numbers.remove(5) #-> Remove the first one 5 integer
numbers.count(100) #-> Count this integer

#Traversal
count = 0
length = len(numbers)
for i in range(length):
    count +=1
    print(f"{i} index holds this value -> {numbers[i]}")

print(count)