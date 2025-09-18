names = {"john","james","alex","mery","ester","samual"}

vowel = "aeiou"

sec_last_vowels = { name for name in names if name[-2] in vowel }

print(sec_last_vowels)