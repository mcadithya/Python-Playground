# Ordered -- Elements maintain the order in which they are inserted.

lst = [10, 20, 30]
print(lst[0])   # 10

# Mutable  -- You can update, add, or remove elements.

lst = [1, 2, 3]
lst[1] = 200
print(lst)      # [1, 200, 3]

# Allows duplicatesc  -- Lists can contain repeated values.

lst = [1, 2, 2, 3]
print(lst)      # [1, 2, 2, 3]

# Stores mixed data types -- Can store integers, floats, strings, even other lists.

lst = [1, "hello", 3.14, [10, 20]]
print(lst)      # [1, 'hello', 3.14, [10, 20]]

#  Supports indexing & slicing  --  Positive & negative indexing, slicing like strings.

lst = [10, 20, 30, 40, 50]
print(lst[0])     # 10
print(lst[-1])    # 50
print(lst[1:4])   # [20, 30, 40]

# Dynamic in size  -- Lists can grow or shrink at runtime.

lst = [1, 2]
lst.append(3)
print(lst)       # [1, 2, 3]

# Can be nested  --  Lists can contain other lists (multi-dimensional lists).

matrix = [[1, 2], [3, 4]]
print(matrix[0][1])   # 2

# Iterable  --  You can loop through list elements.

lst = [10, 20, 30]
for x in lst:
    print(x)
