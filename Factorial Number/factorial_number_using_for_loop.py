#write a program find factorial

num = int(input("Enter the number : "))

fact = 1

for i in range(1,num+1):

    fact = fact * i

   #  i+=1 this is not need becoz here increment by 1
 
print(fact)