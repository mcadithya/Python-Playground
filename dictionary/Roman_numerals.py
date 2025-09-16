# Roman_numerals = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'} 
# write a function that passes an integer as parameter and return the roman letter for that 
# number if that number exists as key else return invalid input
Roman_numerals = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'} 

def roman_numerals(key):

    if key in Roman_numerals:

        print(f"roman letter for {key} is {Roman_numerals[key]}")

    else:

        print("invalid input")

key = int(input("enter the ineger : "))

roman_numerals(key)