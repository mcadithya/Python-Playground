numbers = [1,2,3,4,5,6]

sum = 8

pairs = {(numbers[i],numbers[j]) for i in range(len(numbers)-1) for j in range(i+1,len(numbers)) if numbers[i]+numbers[j] == sum}

print(pairs)