# 1. count(x)  -- Returns the number of times x appears in the tuple.

t = (1, 2, 2, 3, 2)
print(t.count(2))   # 3

# 2. index  -- Returns the first index of element x. Raises ValueError if not found.

t = (10, 20, 30, 20, 40)
print(t.index(20))        # 1
print(t.index(20, 2))     # 3 (search starts from index 2)






