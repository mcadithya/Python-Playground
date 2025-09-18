lst =[18,47,59,18,21,21,63,63]

# unique = []

# for num in lst:
#     if num not in unique:
#         unique.append(num)

# print(unique) #[18, 47, 59, 21, 63]

print(list(set(lst)))   # [47, 18, 21, 59, 63]