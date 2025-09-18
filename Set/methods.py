s = {1, 2, 3}

# add(elem) → Adds an element.
# s.add(4)           # {1, 2, 3, 4}

# update(iterable) → Adds multiple elements.
# s.update([5, 6])   # {1, 2, 3, 4, 5, 6}

# remove(elem) → Removes element (error if not found).
# s.remove(2)        # {1, 3, 4, 5, 6}

# discard(elem) → Removes element (no error if not found).
# s.discard(10)      # no error

# pop() → Removes and returns a random element.
# x = s.pop()        # removes random element

# clear() → Removes all elements.
# s.clear()          # set becomes {}

# copy() → Returns a shallow copy
# c = s.copy()   # {1, 2, 3}


A = {1, 2, 3}
B = {3, 4, 5}

# Set Operations

# union(other) or | → Returns union.
# print(A.union(B))            # {1, 2, 3, 4, 5}

# intersection(other) or & → Returns intersection.
# print(A.intersection(B))     # {3}

# difference(other) or - → Elements in one set but not the other.
# print(A.difference(B))       # {1, 2}

# symmetric_difference(other) or ^ → Elements in either set, but not both.
# print(A.symmetric_difference(B))  # {1, 2, 4, 5}

# difference_update(other) → Removes all elements found in other
# X = {1, 2, 3}
# X.difference_update(B)
# print(X)                       # {1, 2}

# intersection_update(other)
# X = {1, 2, 3}
# X.intersection_update(B)
# print(X)                       # {3}

# isdisjoint(other)
# print(A.isdisjoint(B))         # False (they share 3)

# issubset(other)
# print({1, 2}.issubset(A))      # True

# issuperset(other)
# print(A.issuperset({1, 2}))    # True

