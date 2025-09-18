#write a program that take two input from user and check which on is highest

num_1 = int(input("enter the first number : "))

num_2 = int(input("enter the second number : "))

result= f"{num_1} is highest" if num_1>num_2 else f"{num_2} is highest"

print(result)