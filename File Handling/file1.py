with open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/file1.txt","r") as f:
    
    word_count ={}

    unique_word =[]

    for line in f:

        line = line.rstrip()

        word_list= line.split()

        for word in word_list:
                
                if word in word_count:

                    word_count[word]+=1

                    word_count.update({word:word_count[word]})

                else:
                     
                     word_count.update({word:1})

    for item in word_count: 

        if word_count[item]==1:

            unique_word.append(item)

    print(unique_word)


# methord 2 list -extend - set -list

# with open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/file1.txt","r") as f:
     