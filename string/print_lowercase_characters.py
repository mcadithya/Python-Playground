# write program to print lowercase letters from user string

def check_lowercase(char):

    lowercase_character = ""

    for chr in char:
        
        if chr.islower():

            lowercase_character +=  chr
    
    return lowercase_character

input_string = input("Enter the string : ")

result = check_lowercase(input_string)


print(f"{input_string} contain {len(result)} lowercase letters : {result} ")