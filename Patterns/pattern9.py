# Half Pyramid Patterns in Python using Recursion 
# Enter the rows : 5
# *
# * *
# * * *
# * * * *
# * * * * *


def half_pyramid(rows):

    if rows>0:
        half_pyramid(rows-1)
        print("* "*rows)

input_row= int(input("enter the rows : "))

half_pyramid(input_row)

    
