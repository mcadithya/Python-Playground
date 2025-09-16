words = {"firs1t","s2econd","th3ird","four4th","fi5fth"}

number = { int(chr) for word in words for chr  in word if chr.isdigit()}

print(number)
 