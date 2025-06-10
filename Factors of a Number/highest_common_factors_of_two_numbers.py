# write a program that finds the highest common factor of two numbers

num_1 = int(input("Enter the First number : ")) 

num_2 = int(input("Enter the Second number : ")) 

stop_value = num_1 if num_1<num_2 else num_2

fact=0

for i in range(1,stop_value+1):

    if(num_1 % i==0 and num_2 % i==0):

        fact = i if i>fact else fact

print(fact)