# 8. Half Pyramid Patterns in Python using Loop | Right-Angled Triangle Pattern in Python
# * 
# * * 
# * * * 
# * * * * 
# * * * * *


def half_pyramid(rows):

    for row in range(1,rows+1):

        for col in range(1,row+1):

            print("* ",end="")
        print()
        
        
input_row = int(input("Enter the rows : "))

half_pyramid(input_row)

