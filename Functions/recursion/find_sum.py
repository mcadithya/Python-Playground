def sum_num(num):

    if num >=1:

        print(f"{num} + ",end="")

        return  num + sum_num(num-1)
    
    elif(num ==1):

        print(f"{num} =",end=" ")

        return  num + sum_num(num-1)
    
    else:

        return 0


input_num = int(input("enter the Number : "))

print("=",sum_num(input_num))
