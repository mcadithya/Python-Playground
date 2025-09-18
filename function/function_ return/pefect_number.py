# write a function to check a number perfect or not

def perfect_number(num):

    sum = 0

    for i in range(1,num):
       
       if num % i == 0:
            
            sum +=i

    return sum 
        
input_num = int(input("Enter the number : "))

result = perfect_number(input_num)

if result == input_num:

    print(f"{input_num} is perfect number")
    
else:
     
     print(f"{input_num} is not a perfect number")
