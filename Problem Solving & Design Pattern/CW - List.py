arr = [60, 000, 78, 45, 00, 23, 76, 00, 87, 32, 17]
print(f"Previous List: {arr}")
number = arr.count(0)


for i in range(number):
    arr.remove(0)
    arr.append(0)

print(f"Updated List:  {arr}")