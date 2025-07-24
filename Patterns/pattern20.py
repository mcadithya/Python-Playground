# 20. Number Pyramid Pattern in Python
# Enter the row size for the pattern: 5
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 


def number_pyramid(rows):


    for i in range(1,rows+1):
        
        num = 1

        for space in range(1,rows-i+1):
            
            print(" ",end = " ")

        for j in range (1,2*i):

            if j <= i:

                print(j,end =  " ")

            elif j>i:

                print(i-num,end = " ")
                num+=1
                
        print()

input_value = int(input("enter the row : "))

number_pyramid(input_value)