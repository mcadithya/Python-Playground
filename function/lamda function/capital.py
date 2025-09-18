# words = ['like','we','long','speed']

# output ---- [['l','i','k','e'],['w','e'],['l','o','n','g'],['s','p','e','e','d']]

words = ['like','we','long','speed']

def capital_char(item):

    word =[]

    for chr in item:

        word.append(chr.upper())
        
    return word

capital_characters  = list(map(capital_char,words))

print(capital_characters)

# capital_char = list(map(list, words))

# print(capital_char)
