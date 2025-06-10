# write a program that checks a number is spy number or not

num = int(input("enter the number : "))

num_copy=num

sum = 0

product = 1

for i in range(3):

   digit = num%10

   sum += digit

   product *= digit

   num //= 10

result = f"{num_copy} is spy number" if product == sum else f"{num_copy} is not spy numer"

print(result)