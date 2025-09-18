#5. write a function that returns maximum and minimum number among three numbers

def min_max(*numbers):

    min_value = min(numbers)

    max_value = max(numbers)

    return min_value,max_value

num_1 = int(input("Enter the first number : "))

num_2 = int(input("Enter the second number : "))

num_3 = int(input("Enter the third number : "))

min, max = min_max(num_1,num_2,num_3) 

print(f"The minimum value is {min} and Maximum value is {max} ")
