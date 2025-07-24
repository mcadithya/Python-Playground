# 27. Floyd's Triangle Pattern in Python
# Enter the row size for the pattern: 5
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 


def floyds_triangle(rows):

    num = 1

    for i in range(1,rows+1):

        for j in range(1,i+1):

            print(num, end  = " ")
            num += 1

        print()

input_value = int(input("Enter no. of rows : "))

floyds_triangle(input_value)