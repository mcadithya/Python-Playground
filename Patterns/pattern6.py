# 6. Hollow Pyramid Patterns in Python
#     *    
#    * *   
#   *   *  
#  *     * 
# *********


# def hollow_pyramid(rows):

#     for row in range(1,rows+1):
        
#         for col in range(1,2*rows):

#             if row ==rows or col == rows-row+1 or col == rows+row-1 :

#                 print("*",end = "")

#             else :

#                 print(" ",end = "")

#         print()


# input_rows = int(input("enter the rows : "))
# hollow_pyramid(input_rows)




def hollow_pyramid(rows):

    for row in range(1,rows+1):

        for space in range(rows-row):

            print(" ",end = "")
        
        for col in range(1,2*rows):

            if col == 1 or row == rows or col ==2*row-1:

                print("*",end = "")

            else :

                print(" ",end = "")

        print()


input_rows = int(input("enter the rows : "))

hollow_pyramid(input_rows)