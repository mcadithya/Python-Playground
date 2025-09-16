numbers={1:"one",2:"two",3:"three",4:"four"}

# new_num = numbers.items()

swap_number={}

for key,value in numbers.items():

    swap_number.update({value:key})

print(swap_number)




