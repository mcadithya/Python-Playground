# 19. Inverted Number Right-Angled Triangle Pattern in Python
# Enter the row size for the pattern: 5
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 



def inverted_number(rows):

    for i in range(rows,0,-1):
        num  = 1

        for j in range (i):

            print(num, end = " ")
            num+=1

        print()

input_value = int(input("enter the rows : "))

inverted_number(input_value)