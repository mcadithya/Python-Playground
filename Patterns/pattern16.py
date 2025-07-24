# 16. Hollow Right-Angled Triangle Pattern in Python
# Enter the row size for the pattern: 5
# * 
# * * 
# *   * 
# *     * 
# * * * * * 


def hollow_right_angled_triange(rows):

    for row in range(rows):

        for col in range(row+1):

            if col == 0 or row ==rows-1 or col ==row :

                print("*",end = " ") 

            else:

                print(" ",end  = " ")

        print()

input_value = int(input("enter the rows: "))

hollow_right_angled_triange(input_value)