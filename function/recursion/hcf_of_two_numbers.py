# 1. find the hcf of two numbers using recursion

def hcf(num_1, num_2):

    if num_2 == 0:

        return num_1
    
    else:
        return hcf(num_2, num_1 % num_2)


num_1 = int(input("Enter first number: "))

num_2 = int(input("Enter second number: "))

print("The HCF is:", hcf(num_1, num_2))
     

     

