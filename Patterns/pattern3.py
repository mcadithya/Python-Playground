# 3. Pyramid Patterns in Python with Alphabet

#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E


def abc_pyramid(rows):

   
    for row in range(1,rows+1):

        char = 65

        for space in range(rows-row):

            print(" " , end = "")


        for col in range(1,row+1):

            print(chr(char),end = " ")

            char+=1

        print()


input_rows= int(input("Enter the number of rows : "))

abc_pyramid(input_rows)