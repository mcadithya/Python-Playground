# lst =[16,25,36,49,81] 
# create a list of square roots of number from lst

# squreroot = lambda lst : [num**0.5 for num in lst ]

# input_list=eval(input("Enter list of number with comma separator : "))

# print(squreroot(input_list))


# using map

from math import sqrt

lst=eval(input("Enter list of number with comma separator : "))

squre_root = list(map(sqrt,lst))

print(squre_root)