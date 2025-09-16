# right rotation
#numbers = [1,2,4,6,7,9] 
# 4,6,9,1,2

numbers = [1,2,4,6,7,9] 

rotation_count = 2

for i in range(rotation_count):

    deleted_item = numbers.pop(0)

    # numbers.insert(-1,deleted_item)   cant use insert. last item will shift and insert in last second position

    numbers.append(deleted_item)


print(numbers)