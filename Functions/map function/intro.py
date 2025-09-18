# map()  --- trurn --- map object so need to type casting to set or list, not available in str
# passing value must be iterable --- str,set, list,range,tuple
text = "hello"

converted_txt = list(map(lambda chr : chr.upper(),text))

print(converted_txt)
