# 23. Inverted Alphabet Right-Angled Triangle Pattern in Python
# Enter the row size for the pattern: 5
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 



def inverted_alphabets(rows):

    for i in range(rows,0,-1):

        numeric_value = 65

        for j in range(i):

            print(chr(numeric_value), end = " ")

            numeric_value+=1

        print()

input_value = int(input("enter the no rows : "))

inverted_alphabets(input_value)
        
