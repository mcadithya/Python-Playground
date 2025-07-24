# 18. Hollow Diamond Pattern in Python
# Enter the row size for the pattern: 5
#         * 
#       *   * 
#     *       * 
#   *           * 
# *               * 
#   *           * 
#     *       * 
#       *   * 
#         * 


def hollow_diamond(rows):

    for row in range (0,rows):

        for col in range(0,2*rows-1):

            if col+row ==rows-1 or col - row == rows-1:

                print("*",end = " ")

            else:

                print(" " , end=" ")
        print()

    for row in range (rows-2,-1,-1):

        for col in range(0,2*rows-1):

            if col+row ==rows-1 or col - row == rows-1:

                print("*",end = " ")

            else:

                print(" " , end=" ")
        print()

input_rows= int(input("Enter the number of rows : "))

hollow_diamond(input_rows)