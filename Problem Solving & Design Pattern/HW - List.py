# Method one: remove just the first element
def remove_first_element(arr):
    arr.pop(0)
    print("\n✅ Updated List:")
    print(arr)

# Method two: add the first element as the last
def add_first_as_last(arr):
    first = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]

    arr[-1] = first
    print("\n✅ Updated List:")
    print(arr)

# Main program
arr = list(map(int, input("👉 Enter the elements of the list (space-separated): ").split()))

print("\n------------------ 📌 Menu ------------------")
print("1️⃣   Remove the first element (shift all elements left by 1).")
print("2️⃣   Move the first element to the end (rotate left by 1).")
print("------------------------------------------------")

while(True):
    print("")
    ans = int(input("➡️   Enter your choice (1 or 2): "))

    if ans == 1:
        remove_first_element(arr)
        break

    elif ans == 2:
        add_first_as_last(arr)
        break

    else:
        print("❌  Invalid choice! Please enter 1 or 2.")
        continue