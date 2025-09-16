numbers = (10,11,16,14,23,21,26,68)

# best method is comprahension 

# even_number = tuple([num for num in numbers if num%2==0])

# print(even_number)


even_number  = ()

for num in numbers:

    if num%2==0:

        even_number += (num,)

print(even_number)

