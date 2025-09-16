numbers = {15,26,36,28,14,75,84}

even_num = set()

odd_num  = set()

for num in numbers:

    if num % 2==0:

        even_num.add(num)

    else:

        odd_num.add(num)

print("even number set : ", even_num)

print("odd number set : ", odd_num)