stack = [100, 98, 76, 54, 34]
#Vertical Deta Structure

#Push - Adding something at last:
stack.append(104)
stack.append(45)
print(stack)

#Pop - Just removing the last one:
stack.pop()
print(stack)

#Peek - Showing the last element:
print(stack[-1])

#isEmpty - Just to check if the list exist or not:
def isEmpty(list):
    if(len(list)==0):
        print("Empty")

    else:
        print(f"It has {len(list)} elements.")

isEmpty(stack)