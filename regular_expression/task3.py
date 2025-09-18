# 3) write a program that access all the variable names in variables.txt and check it is a valid variable or not if it is valid then add it to the valid variables.txt
# conditions
#  first character must be alphabets or underscore 
#  variable can only contain underscore ,no spaces,no special characters allowed.
import re 
with open("variable.txt","r") as f1:

    with open("valid_variabe.txt","w") as f2:
         
         pattern = "^[A-Za-z_][A-Za-z0-9_]*$"

         for lines in f1:
              
              lines=lines.rstrip("\n")

              matches = re.fullmatch(pattern,lines)

              if matches:
                   
                   f2.write(f"{lines}\n")


              
