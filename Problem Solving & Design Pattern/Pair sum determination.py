arr = [12, 43, 54, 76, 6, 6, 2, 10]
a = int(input("Enter the sum you want: "))
flag = True

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == a:
            print("Match found:", arr[i], "+", arr[j], "=", a)
            flag = False

if flag:
    print("Not Found")
