#Sorting type algorithm
#Algorithm name -> Bubble sort

#Natural way - methode 1

#Value Assigning
a = 0
b = 10 
print("Fist assigned value stage:",a,b)

temp = a #Temporary variable - assign
a = b #Transform
b = temp #Swap 


#now: a = b, b = temp = a
print("Final result after swap:",a,b)
print("\n----------------------------\n")


#Without 3rd temporary variable in advanced python
c = 100 
d = 50 

print("Before the swap:", c, d)

c,d = d,c #Advanced swap methode
print ("After the swap:", c,d)




print("\n\n ---------------------------------- \n")
# Bubble Sort python array methode 
array = [10234, 98765, 54321, 120000, 87654, 234567, 99999, 456789, 321000, 765432, 888888, 654321, 777777, 432100, 210987, 345678, 567890, 678901, 890123, 999001]
n = len(array)
print(n)

p = 0
s = 0 

for i in range(n):
    for j in range(0, n-1-i):
        p += 1

        if ( array[j] > array[j+1] ):
            array[j], array[j+1] = array[j+1], array[j]
            s = s+1

print("Swaped updated array elements one by one:")
for i in array:
    print(i)
    
print(f"Total number of comparison: {p}")
print(f"Total number of swap: {s}")