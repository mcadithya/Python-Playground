palindrome = lambda lst : [ item for item in lst if item[::-1] == item]


lst = ["radar","malayalam","cycle","eye","nose"]

print(palindrome(lst))