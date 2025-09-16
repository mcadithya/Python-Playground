numbers = (1,2,3,5,7)

rot_count = 2

# output (5,7,1,2,3)



for i in range(rot_count):

    last_item = numbers[-1]

    # rotation_items = (last_item,) + numbers[:-2]

    print(last_item)

    numbers = (last_item,) + numbers[: len(numbers)-1]

print(numbers) 




