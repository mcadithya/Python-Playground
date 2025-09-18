# 1. Case Conversion

# s.upper() → convert to uppercase

# s.lower() → convert to lowercase

# s.title() → capitalize first letter of each word

# s.capitalize() → capitalize first letter of string

# s.swapcase() → swap upper ↔ lower

# s.casefold() → aggressive lowercase (good for comparisons)

"Hello World".lower()     # "hello world"
"HELLO".casefold()        # "hello"

# 2. Search & Find

# s.find(sub) → index of first occurrence (or -1)

# s.rfind(sub) → last occurrence

# s.index(sub) → like find(), but raises ValueError if not found

# s.rindex(sub) → like rfind() but raises error

# s.count(sub) → count occurrences

"banana".find("na")   # 2
"banana".count("a")   # 3


# 3. Check Start / End

# s.startswith(prefix)

# s.endswith(suffix)

"hello.py".endswith(".py")  # True


# 4. Validation (returns True / False)

# s.isalpha() → letters only

# s.isdigit() → digits only

# s.isnumeric() / s.isdecimal() → number checks

# s.isalnum() → alphanumeric

# s.isspace() → whitespace only

# s.isupper() / s.islower() / s.istitle()

"123".isdigit()     # True
"hello".isalpha()   # True


# 5. Whitespace & Trimming

# s.strip() → remove spaces (or chars) both sides

# s.lstrip() / s.rstrip() → left / right only

"   hi   ".strip()   # "hi"


# 6. Replace & Formatting

# s.replace(old, new, count=-1)

# s.format(...) or f-strings

# s.zfill(width) → pad with zeros

"2025".zfill(6)      # "002025"
"Hello {}".format("World")   # "Hello World"


# 7. Split & Join

# s.split(sep=None, maxsplit=-1) → list

# s.rsplit() → split from right

# s.splitlines() → split by newline

# "sep".join(iterable) → join list into string

"one,two,three".split(",")   # ["one","two","three"]
"-".join(["a","b","c"])      # "a-b-c"


# 8. Alignment & Padding

# s.center(width, fillchar)

# s.ljust(width, fillchar)

# s.rjust(width, fillchar)

"cat".center(7, "*")   # "**cat**"

