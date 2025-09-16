text  = "hai hello hai bye good bad bye"

word_list = text.split()

count_dict ={}

for word in word_list:

    if word not in count_dict:

        count_dict[word] = 1

    else:
        
        count_dict[word]+=1

print(count_dict)


