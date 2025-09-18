#filter()  it will return filter object

lst = [1,2,3,4,5,6]

even_num_list = list(filter(lambda num : num%2==0,lst))

print(even_num_list)

print(lst)  