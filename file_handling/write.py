with open("word.txt","r") as f1:

    with open("palindrome.txt","w") as f2:

        with open("non_palindrome.txt","w") as f3:
          
            for word in f1:

                word = word.rstrip("\n")

                if word == word[::-1]:

                    f2.write(f"{word}\n")

                else:
                    
                    f3.write(f"{word}\n")
