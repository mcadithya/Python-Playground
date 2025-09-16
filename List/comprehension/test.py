s = #$%@^&*

if isinstance(s,str):

    if s.isalnum():
        print("True")
    else:
        print("False")
    count=0
    for char in s:
        if char.isalpha():
            count+=1
    if count>1:
        print("True")
    else:
        print("False")
    count_lower =0
    for char in s:
        if char.lower():
            count_lower+=1
    if count_lower>0:
        print("True")
    else:
        print("False")
    count_upper=0
    for char in s:
        if char.upper():
            count_upper+=1
    if count_upper>0:
        print("True")
    else:
        print("False")
        
count_digit =0
for char in s: 
    if char.isdigit():
        count_digit+=1
if count_digit>0:
    print("True")
else:
    print("False")       