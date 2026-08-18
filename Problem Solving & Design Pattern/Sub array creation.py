arr = [10, 56, 78, 90, 89, 45, 68, 92, 34]
n = len(arr)

all_subarray=[]

for i in range(n):
    for j in range(i+1, n+1):
        all_subarray.append(arr[i:j])

for element in all_subarray:
    if(len(element)==3):
        print(element)