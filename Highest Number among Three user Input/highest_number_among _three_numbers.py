# write a program that gives the highest number among three numbers

num_1 = int(input("Enter the First Number : "))

num_2 = int(input("Enter the second Number : "))

num_3 = int(input("Enter the Third Number : "))

num = [num_1, num_2, num_3]

highest = num[0]

for i in range(1,len(num)):

    if num[i] > highest:

        highest = num[i]

print("highest number is :",highest)