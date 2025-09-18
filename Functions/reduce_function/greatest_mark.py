from functools import reduce

student = {"John":98,"James":76,"anna":83,"joseph":99,"stella":78}

result = reduce(lambda std1, std2 : std1 if student[std1]>student[std2] else std2 ,student)

print(result)

# valueslst =student.values()

# result = reduce(max,valueslst)  # reduce(lamda mark1,mark2 mark1 if mark1>mark2 else mark2,valuelst)

# for key in student:
#     if student[key] ==result:
#         print(key)
#         break
