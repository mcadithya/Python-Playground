#calculate Amstrong number

num = int(input("enter the number : "))

num_copy=num

sum = 0

for i in range(3):

    digit = num_copy %10

    sum= digit ** 3

    num_copy//10 

result= f"{num} is Amstrong" if num==sum else f"{num} is not a amstrong number"

print(result)