# write a program that takes a number as  input from user and find the number is perfect or not

num = int(input("Enter the number : "))

num_copy = num

fact_sum = 0

for i in range(1,num_copy):

    if(num_copy % i == 0):

        fact_sum += i

print("fact",fact_sum)

result = f"{num} is perfect" if num == fact_sum else f"{num} is not perfect"

print(result)