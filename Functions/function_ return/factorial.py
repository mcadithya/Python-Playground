# write program to find factorial of given number using params and return

def factorial(num):

    fact = 1

    for i in range(1,num+1):

      fact*=i

    return fact


num = int(input("Enter the Number : "))

print(f"factorial of {num} is",factorial(num))
