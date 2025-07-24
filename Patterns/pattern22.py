# 22. Number Diamond Pattern in Python
# Enter the row size for the pattern: 4
#       1 
#     1 2 1 
#   1 2 3 2 1 
# 1 2 3 4 3 2 1 
#   1 2 3 2 1 
#     1 2 1 
#       1 


def number_diamond(rows):

    for i in range(1,rows+1):

        num =1

        for space in range(rows-i+1):

            print(" ",end = " ")

        for j in range(1,2*i):

            if j<=i:

                print(j, end = " ")

            elif j>i:

                print(i-num , end = " ")

                num+=1
                
        print()

    for i in range(rows-1,0,-1):

        num = 1

        for space in range(rows-i+1):

            print(" ",end  = " ")
        
        for j in range(1,2*i):

            if j<=i:

                print(j,end = " ")

            elif j>i:

                print(i-num,end = " ")

                num +=1
        print()

        
            

        
input_value = int(input("Enter the rows : "))

number_diamond(input_value)


