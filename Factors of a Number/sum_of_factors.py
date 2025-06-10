#write a program find sum of factors of a given number

num = int(input("Enter the number : "))
sum=0
for i in range(1,num+1):

    if(num % i == 0):

       sum+=i

print(f"sum of factors of {num} is",sum)