# 4. Pyramid Patterns in Python with Number
#     1
#    123
#   12345
#  1234567
# 123456789


def number_pyramid(rows):

    for row in range(1,rows+1):

        num = 1 
        
        for space in range(rows-row):

            print(" ", end ="")

        for col in range (1,2*row):

            print(num,end = "")

            num+=1

        print()

input_row= int(input("enter the rows : "))

number_pyramid(input_row)
