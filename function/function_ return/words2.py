lst = [["apple","orange","grapes","pineapple"],["bitter guard","tomato","ginger","broccoli"],["cashew","pista","badam","wallnet"]]

def long_item(item):
    return max(item,key=len)

longest_word = list(filter(long_item,lst))

print(longest_word)