# append(x) → Adds a single element to the end
lst = [1, 2, 3]
lst.append(4)
print(lst)               # [1, 2, 3, 4]

# extend(iterable) → Adds multiple elements (like +=)
lst = [1, 2]
lst.extend([3, 4])
print(lst)               # [1, 2, 3, 4]

# insert(i, x) → Inserts element at index i
lst = [1, 3, 4]
lst.insert(1, 2)
print(lst)               # [1, 2, 3, 4]

# remove(x) → Removes first occurrence of value
lst = [1, 2, 2, 3]
lst.remove(2)
print(lst)               # [1, 2, 3]

# pop([i]) → Removes & returns element at index (default last)
lst = [1, 2, 3]
print(lst.pop())         # 3
print(lst)               # [1, 2]

# clear() → Removes all elements
lst = [1, 2, 3]
lst.clear()
print(lst)               # []

# index(x[, start[, end]]) → Returns index of first occurrence
lst = [1, 2, 3, 2]
print(lst.index(2))      # 1

# count(x) → Returns number of occurrences
lst = [1, 2, 2, 3]
print(lst.count(2))      # 2

# sort(key=None, reverse=False) → Sorts list
lst = [3, 1, 2]
lst.sort()
print(lst)               # [1, 2, 3]

# reverse() → Reverses list in place
lst = [1, 2, 3]
lst.reverse()
print(lst)               # [3, 2, 1]

# copy() → Returns a shallow copy
lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)           # [1, 2, 3]