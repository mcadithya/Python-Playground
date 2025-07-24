# 5. Inverted Full Pyramid Patterns in Python
# *********
#  *******
#   *****
#    ***
#     *


def inverted_pyramid(rows):

    for row in range(rows):

        for space in range(row):

            print(" ",end  = "")
        
        for col in range(2*(rows-row)-1):

            print("*",end = "")

        print()


input_row = int(input("Enter the rows : "))

inverted_pyramid(input_row)



# def inverted_pyramid(rows):

#     for row in range(rows,0,-1):

#         for space in range(rows-row):

#             print(" ",end  = "")
        
#         for col in range(2*row-1):

#             print("*",end = "")

#         print()


# input_row = int(input("Enter the rows : "))

# inverted_pyramid(input_row)
