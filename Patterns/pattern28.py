# 28. Pascal's Triangle Pattern in Python

# To build the pascal triangle, start with “1” at the top, then continue placing numbers below it in a triangular pattern.

# Each number is the numbers directly above it added together.

# Enter the row size for the pattern: 5
#           1   
#         1   1   
#       1   2   1   
#     1   3   3   1   
#   1   4   6   4   1   


def pascals_triangle(rows):

    for i in range(rows):

        for space in range(rows-i):

            print(" ", end = " ")
        
        value = 1

        for j in range(i+1):

            print(f"{value} ", end  = " ")

            value = value * (i - j) // (j+1)

        print()


input_value = int(input("enter no. of rows : "))

pascals_triangle(input_value)

