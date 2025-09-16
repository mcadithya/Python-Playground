numbers={1:"one",2:"two",3:"three",4:"four"}

number_copy = {key:value  for key,value in numbers.items()}

print(number_copy)


num_copy = {key:numbers[key] for key in numbers}

print(num_copy)