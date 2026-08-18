arr = [12, 43, 54, 76]

a = int(input("Enter the sum you want: "))

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == a:
            print("Match found:", arr[i], "+", arr[j], "=", a)
            break   

    else:
        continue
    break

else:
    print("No match found.")
