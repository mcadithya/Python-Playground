d = {"a": 1, "b": 2, "c": 3}

# keys() → Returns all keys

print(d.keys())         # dict_keys(['a', 'b', 'c'])


# values() → Returns all values

print(d.values())       # dict_values([1, 2, 3])


# items() → Returns key-value pairs as tuples

print(d.items())        # dict_items([('a', 1), ('b', 2), ('c', 3)])

# get(key, default) → Returns value of key, or default if key not found

print(d.get("a"))       # 1
print(d.get("z", 0))    # 0


# setdefault(key, default) → Returns value if key exists, otherwise inserts with default value

print(d.setdefault("b", 100))  # 2 (already exists)
print(d.setdefault("z", 99))   # 99 (added new key)
print(d)                       # {'a':1, 'b':2, 'c':3, 'z':99}

# update(other_dict) → Merges another dictionary (overwrites duplicates)

d.update({"b": 200, "d": 4})
print(d)  # {'a': 1, 'b': 200, 'c': 3, 'z': 99, 'd': 4}

# pop(key, default) → Removes and returns value of key

print(d.pop("a"))       # 1
print(d)                # {'b': 200, 'c': 3, 'z': 99, 'd': 4}


# popitem() → Removes and returns last inserted (key, value) pair (since Python 3.7+)

print(d.popitem())      # ('d', 4)


# clear() → Removes all items

d.clear()
print(d)                # {}

# copy() → Returns a shallow copy

d1 = {"x": 1, "y": 2}
d2 = d1.copy()
print(d2)               # {'x': 1, 'y': 2}