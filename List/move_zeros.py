# move all zeros to left with out affecting the insertion order
# numbers = [1,2,5,0,4,0,9,25,0,12]

# [0,0,0,0,1,2,5,4,9,25,12]

numbers = [1,2,5,0,4,0,9,25,0,12]

# zero_count = numbers.count(0)

# for items in numbers:

#     if items ==0:

#         numbers.remove(0)

#  print(numbers)

# new_list = []

# new_list.extend([0]*zero_count)

# new_list.extend(numbers)

# print(new_list)


# for items in numbers:

#     if items == 0:
       
#         # new_List.append(0)

#         numbers.pop()


# for item in numbers:
        
#         if item != 0:
       
#             new_List.append(item)

# print(new_List)


for index in range(len(numbers)):

    if numbers[index]==0:

       zero =  numbers.pop(index)

       numbers.insert(0,zero)

print(numbers)
