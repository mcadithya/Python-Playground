words = {"malayalam","anna","word","python","well","radar","eve","madam","light"}

palindrom = {word for word in words if word[::-1] == word}

print(palindrom)

print(words.difference(palindrom))