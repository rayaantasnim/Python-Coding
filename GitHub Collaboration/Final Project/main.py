#Main functions here
def add(a,b):
    return(a+b)

def substract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

#User input taken
x = float(input("Enter the first number:"))
y = float(input("Enter the second number:"))

#Menu for the user to calculate
print("1. Add the numbers")
print("2. Substract the numbers")
print("3. Multiply the numbers")
print("4. Devide the numbers")
print("5. Exit")

#Procedure for the user
while(True):
    menu = input("Enter the index number of your order to calculate:")

    if(menu == "1"):
        print(f"The result of the addition of the numbers is: {add(x,y)}")

    elif(menu == "2"):
        print(f"The result of the substraction is: {substract(x,y)}")

    elif(menu == "3"):
        print(f"The result of the multiplication is: {multiply(x,y)}")

    elif(menu == "4"):
        if(y == 0.0):
            y = float(input("0 can not be calculated in the divisions. \nTry again:"))

        else:
            print(f"The result of the division of these numbers is: {division(x,y)}")

    elif(menu == "5"):
        print("Exiting from the calculator ... ... ...")
        break 

    else: 
        print("Unvalid Command Given. \nCan't be calculated.")