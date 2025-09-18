from functools import reduce

lst = [15,23,85,96]

result = reduce(lambda item1, item2 : max(item1,item2),lst)  

# result = reduce(lambda item1, item2 : item1 if item1>item2 else item2,lst)

#result = reduce(max,lst)

print(result)