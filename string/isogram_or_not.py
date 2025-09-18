#write program to ckeck given string is isogram or not

input_string  = input("Enter the string : ")


status = "isogram"

for char in input_string:

    if input_string.count(char)>1:

        status = "Not Isogram"

        break


print(status)


