# 24. Alphabet Pyramid Pattern in Python
# Enter the row size for the pattern: 5
#         A 
#       A B A 
#     A B C B A 
#   A B C D C B A 
# A B C D E D C B A 


def alphabet_pyramid(rows):

    for i in range(1,rows+1):

        char_value = 65

        for space in range(rows-i):

            print(" ", end = " ")

        for j in range(1, 2*i):

            print(chr(char_value),end = " ")

            if j < i:

                char_value += 1

            else:

                char_value -= 1

        print()


input_value = int(input("enter the no: of rows : "))

alphabet_pyramid(input_value)