 

def check_character(char):

    result = ""

    # if char in "a"<char<"z" or "A"<char<'Z':
    # if char.isalpha() == True:
    if type(char)== str:
     
     result= "entered characher is Alphabet"
    

    elif char.isdigit() ==True:

        result = " Entered character is number"

    elif(char==" "):
       
       result = "entered character is space "

    else:
       
       result = "entered character is symbol"

    return result

char = input("enter the character : ")

print(check_character(char))

