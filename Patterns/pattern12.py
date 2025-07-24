# 12. Inverted Pyramid Patterns in Python | Inverted Right-Angled Triangle in Python
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


def inverted_haf_pyramid(rows):

    for row in range(rows,0,-1):

        for col in range (row):

            print("*",end = " ")

        print()


input_row = int(input("enter the row : "))

inverted_haf_pyramid(input_row)