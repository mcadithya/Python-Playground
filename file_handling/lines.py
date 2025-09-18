# f = open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/lines.txt","r")

# word_dic = {}
# line_num = 1
# for sentance in f:


#     sentance = sentance.rstrip("\n")

#     # print("sentance",sentance)

#     count = 0

#     split_word = sentance.split()

#     print(split_word,"split")

#     for wors in split_word:

#         count+=1

#     word_dic.update({f"Line {line_num}":count})

#     line_num+=1

# print(word_dic)

f = open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/lines.txt","r")

word_dic = {}

line_num = 1

for sentance in f:

    sentance = sentance.rstrip("\n")

    split_word = sentance.split()

    value = len(split_word)

    word_dic.update({f"Line {line_num}":value})

    line_num+=1

print(word_dic)





    
    