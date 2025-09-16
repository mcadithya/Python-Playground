numbers = (0,1,2,0,3,0,7,5,0,7) 

# zeros=()

# for number in numbers:

#     if number == 0:

#         zeros+=(number,)

# non_zero_ele = ()

# for num in numbers:

#     if num !=0:

#         non_zero_ele+=(num,)


# print(zeros+non_zero_ele)

zeros= ()

non_zero =()

for num in numbers:

    if num == 0 :

       zeros += (0,)

    else:
        
        non_zero += (num,)

print(zeros + non_zero)

