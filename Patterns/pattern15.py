# 15. Hollow Square Pattern in Python
# Enter the row size for the pattern: 5
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 




def hollow_square(rows):

    for row in range(rows):

        for col in range(rows):
            if col ==rows-1 or row ==0 or col ==0 or row ==rows-1:

                print("*", end  = " ")
            else:
                print(" ",end = " " )
        print()


input_value = int(input("enter the rows: "))

hollow_square(input_value)
