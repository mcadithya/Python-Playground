# write a program that checks a number disarium or not using for loop

num = int(input("enter the number : "))

num_copy = num 

converted_num = str(num_copy)

Stop_value = len(converted_num)

sum=0

for i in range (Stop_value):

    digit = num_copy % 10

    sum += digit ** Stop_value

    num_copy//=10

    Stop_value -= 1

result = f"{num} is disarium" if sum == num else f"{num} is not disarium"

print(result)