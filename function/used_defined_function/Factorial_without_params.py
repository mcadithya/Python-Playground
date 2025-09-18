# write a function that takes a number as input from user and function displays factorial of that number
# 1. without param without return


def factorial():
    
    num  = int(input("Enter the Number : "))

    fact = 1

    for i in range(1,num+1):

        fact = fact * i

    print(f"Factorial of {num} is {fact}")

factorial()
