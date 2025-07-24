# 11. Half Pyramid Patterns in Python in Alphabets | Alphabet Right-Angled Triangle Pattern in Python
# A 
# B B 
# C C C 
# D D D D 
# E E E E E


def alphabet_half_pyramid(rows):
    char =65
    for row in range(1,rows+1):

        for col in range (1,row+1):

            print(chr(char),end = " ") 
        
        print()
        
        char += 1


input_row = int(input("enter the row : "))

alphabet_half_pyramid(input_row)