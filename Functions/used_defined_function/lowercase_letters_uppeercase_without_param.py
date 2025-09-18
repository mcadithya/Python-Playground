# with param without return

def countLoop(text):

    upercase_count=0

    lowercase_count=0
    
    for char in text:

        if('A' <= char <= 'Z'):

            upercase_count+=1

        elif('a' <= char <= 'z'):

            lowercase_count+=1

    print(f"lowercase count : {lowercase_count}")
    
    print(f" uppercase count :{upercase_count}")

text=input("Enter the string : ")

countLoop(text)
