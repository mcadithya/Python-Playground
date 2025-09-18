from functools import reduce

students = {"John":98,"James":76,"anna":83,"joseph":99,"stella":78}

values_lst = students.values()

# sum_value = reduce(lambda item1, item2 : item1+item2,values_lst)

# avrge = sum_value//len(students)

# filter_names = list(filter(lambda name : students[name]>=avrge,students))

# print(filter_names)





filter_name = list(filter(lambda name : students[name]>= reduce(lambda item1, item2 : item1+item2,values_lst)//len(students),students))

print(filter_name)