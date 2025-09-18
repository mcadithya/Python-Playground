# write a program to find source and target are anagram pairs

# source ='silent'

# target ='listen'


def anagram(source,target):

    status = "string is anagram"

    source = source.replace(" ","").lower()

    target = target.replace(" ","").lower()
    
    if len(source) != len(target):

        status = "string is not anagram"
    
    else:
   
        for char in source:

            if source.count(char)!=target.count(char):

                status = "string is not anagram"

    return status

input_source = input("Enter the source string : ")

input_target = input("Enter the target string : ")

result = anagram(input_source,input_target)

print(result)
