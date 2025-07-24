# 10. Pyramid Patterns in Python with Numbers | Number Right-Angled Triangle Pattern in Python
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def number_half_pyramid(rows):

    for row in range(1,rows+1):
        
        num =1

        for col  in range(1,row+1):

            print(num,end = " ")

            num+=1
    
        print()

input_row= int(input("Enter the Row : "))

number_half_pyramid(input_row)