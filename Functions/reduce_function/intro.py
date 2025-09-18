# not buit in function

#functools

from functools import reduce

# reduce(function,iterable) -- it return single value it may be int,str...

# function(param1,param2)

lst = [15,23,85,96]

result = reduce(lambda item1, item2 : item1+ item2,lst)

print(result)