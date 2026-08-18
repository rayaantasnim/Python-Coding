#Step 1 - Start 
#Step 2 - Take user input 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#Step 3 - Comparing the number 
def large_number(a,b):
    if (a>b):
        return(a)

    elif (a<b):
        return(b)

    else:
        return("No inputed integer")

#Step 4 - Keeping the large number 
large = large_number(a,b)

#Step 5 - Printing the largest number 
print (f"{large} is the larger number.")

#Step 6 - End program