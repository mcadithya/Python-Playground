# 17. Hollow Inverted Right-Angled Triangle Pattern in Python
# Enter the row size for the pattern: 4
# * * * * 
# *   * 
# * * 
# * 


def inverted_hollow_triangle(rows):

    for row in range(rows,0,-1):

        for col in range(row):

            if row==rows or col ==0 or col ==row-1:

                print("*",end = " ")
            else:

                print(" ", end = " ")
        print()

input_value = int(input("Enter the rows: "))

inverted_hollow_triangle(input_value)


 
