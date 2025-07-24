# 1 . Full Pyramid Patterns in Python using Loop
#     *
#    ***
#   *****
#  *******
# *********

def full_pyramid(n):

    for row in range (1,n+1):

        for space in range(n - row):

            print(" ",end = "")

        for col in range (2*row-1):

            print("*",end = "")

        print()

# using single loop


# def full_pyramid(rows):

#     for row in range (1,rows+1):

#         print(" " * (rows - row), end=" ")       # single‑width leading spaces
#         print("*" * (2*row - 1)) 
   

input_rows = int(input("Enter the number of rows : "))
full_pyramid(input_rows)







