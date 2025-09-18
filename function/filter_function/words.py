#len>=7

lst = [["apple","orange","grapes","pineapple"],["bitter guard","tomato","ginger","broccoli"],["cashew","pista","badam","wallnet"]]

def long_item(item):

    longest_word = list(filter(lambda w : [w for x in item if len(w)>=7], item))
    
    return longest_word

longest_word =list(map(long_item,lst)) 

print(longest_word)


