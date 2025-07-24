def is_armstrong_number(num):

    sum = 0

    length = len(str(num))


    for n in range(length):

        digits = num%10

        sum+=digits**length

        num//=10

    return sum


input_num = int(input("Enter the number : "))



sum = is_armstrong_number(input_num)

if sum ==input_num:

    print("given num is armstrong")
    
else:
    print("no")