def factorial(num):
    
    if num ==0 or num ==1:

        return 1
    
    else:
        return num * factorial(num - 1)
    
input_value = int(input("enter the number : "))

print(factorial(input_value))
  