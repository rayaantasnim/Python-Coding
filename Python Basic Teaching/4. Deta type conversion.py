from math import *

string = "2562112"
integer = 158796764265
float_value = 1087868.999999999999
bulliyan = True

#String to Integer
if(string and integer):
    print("String here:", string)
    print("Added with", integer)
    #print(string+integer)

    string_as_integer = int(string)
    print("\n\nConverted as integer:", string_as_integer)
    print("Final result as added with", integer, "is:", string_as_integer+integer)

#Integer to String
if(string and integer):
    integer_as_string = str(integer)
    print("\n\nUpdated integer as a string deta:",integer_as_string)
    addition = string + integer_as_string
    print(addition)

#Float to Integer
if(float_value):
    float_value_as_integer = floor(float_value)
    print("Float value as an advanced converted integer: ", float_value_as_integer)

    #Advanced way with low lack:
    float_value_as_integer = int(float_value)
    print("Float value converted as an integer: ", float_value_as_integer)

print("")
#Bulliyan : True to False
if(bulliyan):
    print("It is true now.")
    bulliyan = False

#Bulliyan : False to True
if(bulliyan):
    print("Second time : It is true still.")

if not bulliyan:
    print("It is false now.!!!")
    print(bulliyan)