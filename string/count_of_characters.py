def character_count(char):

    alpha_count = 0

    num_count = 0

    space_count = 0

    symbol_count = 0

    for chr in char:

        if chr.isalpha()==True:

            alpha_count+=1

        elif(chr.isdigit()==True):

            num_count+=1

        elif(chr.isspace() == True):

            space_count+=1

        else:

            symbol_count+=1

    return alpha_count,num_count,space_count,symbol_count



string_input = input("enter the string : ")

alpha_count,num_count,space_count,symbol_count = character_count(string_input)

print(f"Inside {string_input} have {alpha_count} alphabets, {num_count} numbers, {space_count} spaces, { symbol_count} symbols")