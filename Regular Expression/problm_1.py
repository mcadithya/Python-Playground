from re import finditer

text ="abc12z3cghcgf4s7out"

pattern ="[a-z][0-9]"  # aphabets followed by number

matches = finditer(pattern,text)

for match in matches:

    print(match.start(),match.group()) 