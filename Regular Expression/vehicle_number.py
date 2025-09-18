#write a regular expression to check a vehicle registration number is valid or not
import  re

pattern  ="[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}"

vehicle_number  = input("enter your vehicle number: ")

matches = re.fullmatch(pattern,vehicle_number)

if matches:

    print("vehicle number is valid")

else:
    
    print("vehicle number is not valid")
    