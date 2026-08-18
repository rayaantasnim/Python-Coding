arr = [500, 900, 456, 987, 984, 785, 876, 423, 981, 98, 12, 45, 89, 123, 456, 1]
l = len(arr)

minimum = arr[0]

for i in range(1, l):
    if (arr[i] < minimum):
        minimum = arr[i]

print(minimum)
