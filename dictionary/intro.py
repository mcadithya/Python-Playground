# Features of Dictionary in Python
# 1. Key-Value Pairs  --  Data is stored as {key: value} pairs.

student = {"name": "Alice", "age": 20}
print(student["name"])   # Alice


# 2. Unordered (Python < 3.7) / Ordered (Python 3.7+)  --  Since Python 3.7+, dictionaries preserve insertion order by default.

d = {"a": 1, "b": 2, "c": 3}
print(d)   # {'a': 1, 'b': 2, 'c': 3} (order preserved)

# 3. Mutable  --  You can add, update, or delete items.

d = {"a": 1, "b": 2}
d["c"] = 3        # add
d["a"] = 100      # update
print(d)          # {'a': 100, 'b': 2, 'c': 3}

# 4. Unique Keys  --  Keys must be unique. If a duplicate key is added, the last value overrides the previous.

d = {"a": 1, "a": 2}
print(d)   # {'a': 2}


# 5. Keys must be Immutable  --  Keys can be int, str, tuple, etc. but not mutable types like lists.

d = {(1,2): "point", "name": "Bob"}
print(d[(1,2)])   # point

# 6. Values can be of Any Type  --  Values may be numbers, strings, lists, dictionaries, or even functions.

d = {"id": 1, "name": "Eve", "marks": [85, 90]}
print(d["marks"])   # [85, 90]

# 7. Dynamic Size  --  Dictionaries can grow or shrink at runtime.

d = {}
d["x"] = 10
print(d)   # {'x': 10}
student = {"name":"john","age":18,"class":11}

# 8. Efficient Lookup  --  Very fast for searching keys (O(1) average time).

d = {"a": 1, "b": 2}
print("b" in d)   # True

# 9. Nested Dictionaries  --  Dictionaries can contain other dictionaries.

student = {
    "name": "Tom",
    "marks": {"math": 90, "science": 85}
}
print(student["marks"]["math"])  # 90
