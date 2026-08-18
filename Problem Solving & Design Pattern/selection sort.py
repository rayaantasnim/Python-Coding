array = [64, 25, 12, 22, 11, 101, 204, 109, 503, 876, 980, 987, 678]
n = len(array)


a = 0 
for i in range(n):
    min_index = i 
    for j in range(i + 1, n):
        if (array[j] < array[min_index]):
            min_index = j 
    array[i], array [min_index] = array[min_index], array[i]
    a +=1

print ("The Sorted array:", array)
print ("Number of swaps: ->", a)