# 14. Diamond Pattern in Python
#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

def diamond(rows):

    for row in range (rows):

        for space in range(rows-row):
            print(" ",end=" ")

        for col in range(2*row+1):

            print("*",end = " ")
        
        print()

    for row in range(rows-1,0,-1):

        for space in range(rows-row+1):

            print(" ",end = " ")

        for col in range(2*row-1):

            print("*",end = " ")
            
        print()

input_value = int(input("enter the rows: "))

diamond(input_value)