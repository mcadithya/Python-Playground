# 2)  write a program that checks the input gstn number is valid or not
# Conditions :
# 1.first 2 numbers
# 2.next 10 characters are pan number
# 3.next character is a number
# 4.next character is Z by default
# 5.last character is either alphabet or digit


import  re

pattern  ="[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9]Z[A-Z0-9]"

gstn  = input("enter your gstn number: ")

matches = re.fullmatch(pattern,gstn)

if matches:

    print("vehicle number is valid")

else:
    
    print("vehicle number is not valid")
