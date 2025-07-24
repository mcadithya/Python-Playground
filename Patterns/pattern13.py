# 13. Hollow Inverted Half Pyramid in Python
# *****
#  *  *
#   * *
#    **
#     *

def hollow_inverted_half_pyramid(rows):

    for row in range(rows):

        for space in range(row):

            print(" ", end="")

        for col in range(rows - row):

            if col == 0 or col == rows - row - 1 or row==0:

                print("*", end="")

            else:

                print(" ", end="")

        print()



input_row = int(input("enter the rows : "))

hollow_inverted_half_pyramid(input_row)

