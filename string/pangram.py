# text = 'the quick brown fox jumps over the lazy dog' 
text = "asdffgvf "
# text contails all Alphabet

english_alphabet = "abcdefghijklmnopqrstuvwxyz"

def pangram(text):

    alphabet = ""

    text = text.replace(" ","")

    for i in text:

        if alphabet.find(i)==-1:
           
            alphabet = alphabet+i
            
        else:

            continue
            
    return alphabet



alphabet = pangram(text)

print(alphabet)

if len(english_alphabet) == len(alphabet):

    print("pangram")

else:

    print("not pangram")





