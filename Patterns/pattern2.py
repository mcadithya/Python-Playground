# Full Pyramid Patterns in Python Recursion

def print_space(space):

    if space > 0:

        print(" ",end="")

        print_space(space-1)



def print_astric(astric):

    if astric > 0:

        print("*",end = "")

        print_astric(astric-1)



def full_pyramid(rows,current_row = 1):

    if current_row>rows:

        return
    
    spaces   = rows-current_row

    astrics = 2 * current_row-1

    print_space(spaces)

    print_astric(astrics)

    print()

    full_pyramid(rows,current_row+1)


input_rows = int(input("enter the row : "))

full_pyramid(input_rows)



