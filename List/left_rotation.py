#write a program to rotate number in 2 anticlockwise(left rotation)
# [7, 9, 1, 2, 4, 6]
numbers = [1,2,4,6,7,9]

rotation_count = 2

for i in range(rotation_count):

    deleted_item = numbers.pop()

    numbers.insert(0,deleted_item)

print(numbers)