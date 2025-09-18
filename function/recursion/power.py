def power(num_1,num_2):
    
    if num_2 >0:
       
       return num_1 * power(num_1,num_2-1)
    
    else:
        
        return 1

val = power(5,2)

print(val)