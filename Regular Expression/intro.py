# module  -- re

# regular expresion use for pattern validation and pattern identification

from re import finditer

# finditer()

# finditer(pattern,text)   --- it is iterator  -- it return a type of iterator object 

text = "pneumonoultramicroscopicsilicovolcanoconiosis" 

pattern  = "[a-zA-Z0-9]"# pattern  = "[a-z]" # pattern  = "[a-e]" # pattern  = "[abcd]" # pattern  = "[uo]" #  pattern  = "on" # pattern  = "a" 

matches = finditer(pattern,text)

for match in matches:
    print(match.start(),match.group())   # start()  --return index of the pattern , group return the pattern


#if i wnat u or O  ===  pattern  = [uo]



