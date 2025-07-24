# 7. Hollow Inverted Pyramid Pattern in Python
# Enter the row size for the pattern: 5
# * * * * * * * * * 
#   *           * 
#     *       * 
#       *   * 
#         * 

def inverted_hollow_pyramid(rows):

    for row in range(rows,0,-1):

        for space in range(rows-row):
 
            print(" ",end = " ")
        
        for col in range(1,2*rows):

            if row==rows or col ==2*row-1 or col ==1:

                print("*",end = " ")

            else:

                print(" " , end = " ")
        print()


input_row = int(input("enter the rows : "))

inverted_hollow_pyramid(input_row)
